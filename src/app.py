import json

from flask import request

from src import create_app
from src.models import Cats, db

app = create_app()

@app.route('/', methods=['GET'])
def add():
    data = request.get_json()
    name = data['name']
    price = data['price']
    breed = data['breed']

    cat = Cats(name=name, price=price, breed=breed)
    db.session_add(cat)
    db.session_commit()
    return json.dumps("Added"), 200

@app.route('/remove/<cat_id>', methods=['DELETE'])
def remove(cat_id):
    Cats.query.filter_by(id=cat_id).delete()
    db.session_commit()
    return json.dumps("Deleted"), 200


@app.route('/edit/<cat_id>', methods=['PATCH'])
def edit(cat_id):
    data = request.get_json()
    new_price = data['price']
    cat_to_update = Cats.query.filter_by(id=cat_id).all()[0]
    cat_to_update.price = new_price
    db.session_commit()
    return json.dumps("Edited"), 200