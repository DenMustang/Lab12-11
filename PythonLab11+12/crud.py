from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from flask_marshmallow import Marshmallow
import json
import copy


with open("secret.json") as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(35), unique=False)
    weight_in_kg = db.Column(db.Integer, unique=False)
    description = db.Column(db.String(35), unique=False)
    name_of_exhibit = db.Column(db.String(35), unique=False)
    decade = db.Column(db.Integer, unique=False)
    age = db.Column(db.Integer, unique=False)
    type_of_weapon = db.Column(db.String(35), unique=False)

    def __init__(self, author=None, weight_in_kg=0.0, description=None, name_of_exhibit=None,
                 decade=0.0, age=0.0, type_of_weapon=None):
        self.author = author
        self.weight_in_kg = weight_in_kg
        self.description = description
        self.name_of_exhibit = name_of_exhibit
        self.decade = decade
        self.age = age
        self.type_of_weapon = type_of_weapon

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


db.create_all()


class WeaponSchema(ma.Schema):
    class Meta:
        model = Weapon
        sql_session = db.session

    id = fields.Integer(dump_only=True)
    author = fields.String(required=True)
    weight_in_kg = fields.Integer(required=True)
    description = fields.String(required=True)
    name_of_exhibit = fields.String(required=True)
    decade = fields.Integer(required=True)
    age = fields.Integer(required=True)
    type_of_weapon = fields.String(required=True)


weapon_schema = WeaponSchema()
many_weapon_schemas = WeaponSchema(many=True)


@app.route("/weapons", methods=["GET"])
def get_all_weapons():
    weapons = Weapon.query.all()
    if not weapons:
        abort(404)
    weapons = many_weapon_schemas.dump(weapons)
    return make_response(jsonify({"weapons": weapons}), 200)


@app.route("/weapons/<id>", methods=["GET"])
def get_weapon_by_id(id):
    get_weapon = Weapon.query.get(id)
    if not get_weapon:
        abort(404)
    weapon = weapon_schema.dump(get_weapon)
    return make_response(jsonify({"weapon": weapon}), 200)


@app.route("/weapons", methods=["POST"])
def add_weapon():
    author = request.json['author']
    description = request.json['description']
    weight_in_kg = request.json['weight_in_kg']
    name_of_exhibit = request.json['name_of_exhibit']
    decade = request.json['decade']
    age = request.json['age']
    type_of_weapon = request.json['type_of_weapon']
    weapon = Weapon(author=author, weight_in_kg=weight_in_kg, description=description,
                    name_of_exhibit=name_of_exhibit, decade=decade, age=age, type_of_weapon=type_of_weapon)
    db.session.add(weapon)
    db.session.commit()
    return weapon_schema.jsonify(weapon)


@app.route("/weapons/<id>", methods=["PUT"])
def update_weapon_by_id(id):
    data = request.get_json()
    get_weapon = Weapon.query.get(id)

    old_weapon = copy.deepcopy(get_weapon)
    if data.get("author"):
        get_weapon.author = data["author"]
    if data.get("weight_in_kg"):
        get_weapon.weight_in_kg = data["weight_in_kg"]
    if data.get("description"):
        get_weapon.description = data["description"]
    if data.get("name_of_exhibit"):
        get_weapon.name_of_exhibit = data["name_of_exhibit"]
    if data.get("decade"):
        get_weapon.decade = data["decade"]
    if data.get("age"):
        get_weapon.age = data["age"]
    if data.get("type_of_weapon"):
        get_weapon.type_of_weapon = data["type_of_weapon"]

    db.session.add(get_weapon)
    db.session.commit()
    return weapon_schema.jsonify(old_weapon)


@app.route("/weapons/<id>", methods=["DELETE"])
def delete_weapon_by_id(id):
    get_weapon = Weapon.query.get(id)
    if not get_weapon:
        abort(404)
    db.session.delete(get_weapon)
    db.session.commit()
    return make_response("", 200)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="127.0.0.1", port="8080")
