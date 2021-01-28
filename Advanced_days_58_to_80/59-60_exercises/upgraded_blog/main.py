from flask import Flask, render_template, request   
import requests

app = Flask(__name__)

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
    


if __name__ == "__main__":
    app.run(debug=True)