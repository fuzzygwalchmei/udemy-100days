from flask import Flask, render_template, request   
import requests

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CsrfProtect

from flask_bootstrap import Bootstrap



class Login(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Submit")



app = Flask(__name__)

csrf = CsrfProtect(app)
app.secret_key = "some rando string"
Bootstrap(app)

blog_endpoint = 'https://api.npoint.io/43644ec4f0013682fc0d'
posts = requests.get(blog_endpoint).json()

# testing

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', all_posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts/<int:index>')
def post(index):
    requested_post = None
    for post in posts:
        if post["id"] == index:
            requested_post = post
    return render_template('post.html', post = requested_post)


@app.route('/form-entry', methods=['POST'])
def submit():
    error = None
    if request.method == 'POST':
        print(request.form['name'])
        print(request.form)
        return render_template('form-entry.html')
    return render_template('contact.html')
    
@app.route('/login', methods=["GET","POST"])
def login():
    success = "Pending"
    login_form = Login()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '123456':
            success = "Success"
        else:
            success = "Failure"
    return render_template('login.html', form=login_form, success = success)

if __name__ == "__main__":
    app.run(debug=True)