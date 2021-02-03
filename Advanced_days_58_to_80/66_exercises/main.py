from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
from sqlalchemy.sql.expression import column

from sqlalchemy.sql.schema import Column

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name:getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

    

## HTTP GET - Read Record
@app.route('/all')
def get_all():
    cafes = db.session.query(Cafe).all()
    all_cafes = {cafe.id:cafe.to_dict() for cafe in cafes}
    return jsonify(all_cafes)

@app.route('/random')
def get_random():
    cafes = db.session.query(Cafe).all()
    cafe = choice(cafes)
    return jsonify(cafe.to_dict())

@app.route('/search')
def get_area():
    area = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=area).first()
    if cafe:
        return jsonify(cafe.to_dict())
    return jsonify(error={"Not Found":"Sorry, this area appears to not have any cafes"})



## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def post_new():
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('loc'),
        has_sockets = bool(request.form.get('sockets')),
        has_toilet = bool(request.form.get('toilets')),
        has_wifi = bool(request.form.get('wifi')),
        can_take_calls = bool(request.form.get('calls')),
        seats = request.form.get('seats'),
        coffee_price = request.form.get('coffee_price')
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {"success":"Successfully added the new cafe"})

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PUT'])
def update_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe and request.form.get('new_price'):
        cafe.coffee_price = request.form.get('new_price')
        db.session.commit()
        return jsonify(response={"success":"Successfully update"})
    elif not cafe:
        return jsonify(response={"failure":"Cafe id does not exist"})
    elif not request.form.get('new_price'):
        return jsonify(response={"failure":"No price supplied"})
    else:
        return jsonify(response={"wtf":"Not sure how i got here"})

## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>')
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"Success":"Cafe was deleted"})
    else:
        return jsonify(error={"Failure":"Record was not deleted for some reason, likely it didnt exist"})


if __name__ == '__main__':
    app.run(debug=True)
