from flask import Flask
from random import randint

app = Flask(__name__)

guess_it = randint(1,10)


@app.route('/')
def home():
    return "This will let you guess a number between 1 and 10. Just add the number to the address (eg http://127.0.0.1:5000/5)"

@app.route('/<int:guess>')
def guessing(guess):
    if guess == guess_it:
        return "<h1 style='color: green'>You guess it!</h1>"
    elif guess < guess_it:
        return "<h1 style='color: blue'>Too low</h1>"
    else:
        return "<h1 style='color: red'>Too High</h1>"







if __name__ == "__main__":
    app.run(debug=True)