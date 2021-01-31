from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):

    id  = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f'<Book {self.id} - {self.title} - {self.author} - {self.rating}'

db.create_all()

# all_books = []

@app.route('/')
def home():
    
    all_books = db.session.query(Books).all()    
    return render_template('index.html', data = all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        # all_books.append({
        #     'title': request.form['title'],
        #     'author': request.form['author'],
        #     'rating': request.form['rating']
        # })
        book = Books(title = request.form['title'], author = request.form['author'], rating = request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template('add.html')


@app.route('/edit', methods=['GET','POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        print(book_id)
        book = Books.query.get(book_id)
        print(book)
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for("home"))
    book = Books.query.get(request.args.get('id'))
    return render_template('edit.html', book = book)

@app.route('/delete')
def delete():
    book = Books.query.get(request.args.get('id'))
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

