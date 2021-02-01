from flask import Flask, render_template, redirect, url_for, request
from flask.templating import render_template_string
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
from os import getenv
import requests
import requests_cache




load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('sqlite_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

TMDB_API = getenv('tmdb_api')
requests_cache.install_cache('demo_cache')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Integer)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    image_url = db.Column(db.String(250))

class RateMovieForm(FlaskForm):
    rating = StringField("Your rating out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add a movie")

db.create_all()



Bootstrap(app)


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/add', methods=['GET','POST'])
def add():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        params = {'api_key': TMDB_API, 'query': movie_title}
        url = 'https://api.themoviedb.org/3/search/movie'
        resp = requests.get(url=url,  params=params)
        resp.raise_for_status()

        result = resp.json()['results']
        return render_template("select.html", options = result)
    return render_template("add.html", form=form)
       


@app.route('/select')
def select():
    movie_id = request.args.get('id')
    if movie_id:
        params = {'api_key': TMDB_API, "language": "en-US"}
        url = f'https://api.themoviedb.org/3/movie/{movie_id}'
        resp = requests.get(url=url,  params=params)
        resp.raise_for_status()

        result = resp.json()
        movie = Movie(
            title = result['original_title'],
            year = result['release_date'],
            description = result['overview'],
            image_url = f"https://image.tmdb.org/t/p/w500{result['backdrop_path']}"
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id = movie.id))


@app.route('/edit', methods=['GET','POST'])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))    
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    movie = Movie.query.get(request.args.get('id'))
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
