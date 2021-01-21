from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data = {}
    return render_template("index.html",
     random=random.randint(1,10), 
     copy_year = dt.datetime.now().strftime('%Y'), data=data)


@app.route('/guess/<name>')
def guess(name):
    r = requests.get(f'https://api.genderize.io?name={name}')
    r.raise_for_status()
    data = r.json()
    return render_template('index.html', data = data,
     random=random.randint(1,10), 
     copy_year = dt.datetime.now().strftime('%Y'))


if __name__ == "__main__":
    app.run(debug=True)