import os
import pymongo
from flask import Flask, jsonify, request, abort
from model import db, People

app = Flask(__name__)
app.config['MONGODB_DB'] = os.environ.get('MONGODB_DB', 'b8dhxfi0ekhvlxy')
app.config['MONGODB_HOST'] = os.environ.get('MONGODB_HOST', 'b8dhxfi0ekhvlxy-mongodb.services.clever-cloud.com')
app.config['MONGODB_PORT'] = int(os.environ.get('MONGODB_PORT', 27017))
app.config['MONGODB_USERNAME'] = os.environ.get('MONGODB_USERNAME', 'uo58xejln7ujk0x0v7mt')
app.config['MONGODB_PASSWORD'] = os.environ.get('MONGODB_PASSWORD', 'leUMfDV4AbXhkdNyVeJI')

db.init_app(app)

def get_by_id(id):
    item = People.objects(id=id).first()
    if not item:
        return abort(404)
    return item


@app.route('/', methods=['GET'])
def health():
    return jsonify({'api': 'ok'}), 200


@app.route('/people', methods=['GET'])
def get_all():
    people = People.objects
    return jsonify({
        'list': [x.to_json() for x in people]
    })

@app.route('/people', methods=['POST'])
def create():
    item = People()

    name = request.json.get('name')
    age = request.json.get('age')

    if not name or not age:
        return jsonify({
            'error': 'nombre y edad requeridos'
        })
    
    item.name = name
    item.age = age

    item.save()
    id = str(item.id)

    return jsonify({
        'id': id,
        'resource': f'/people/{id}'
    }), 201

@app.route('/people/<string:user_id>', methods=['GET'])
def get_item(user_id):
    item = get_by_id(user_id)
    return jsonify(item.to_json()), 200

@app.route('/people/<string:user_id>', methods=['PATCH'])
def update_item(user_id):
    item = get_by_id(user_id)

    name = request.json.get('name')
    if name:
        item.name = name

    age = request.json.get('age')
    if age:
        item.age = age

    item.save()
    return jsonify(''), 200

@app.route('/people/<string:user_id>', methods=['DELETE'])
def delete_item(user_id):
    item = get_by_id(user_id)
    item.delete()
    return jsonify(''), 204
