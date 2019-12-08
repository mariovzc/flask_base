import os
from model import db, People
from flask import Flask, jsonify, request, abort
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_URI', 'mysql+pymysql://udsxgelteuzxqbry:53VxTLH0SPZpCug0L0xB@be16hdjcuvwjahwcr6bn-mysql.services.clever-cloud.com:3306/be16hdjcuvwjahwcr6bn')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_recycle': os.environ.get('SQLALCHEMY_POOL_RECYCLE', 1800),
    'pool_timeout': os.environ.get('SQLALCHEMY_POOL_TIMEOUT', 30),
    'pool_size': os.environ.get('SQLALCHEMY_POOL_SIZE', 5),
    'max_overflow': os.environ.get('SQLALCHEMY_MAX_OVERFLOW', 2),
    'pool_pre_ping': os.environ.get('SQLALCHEMY_PRE_PING', 1) == 1,
}
db.init_app(app)

def get_by_id(id):
    item = People.query\
                 .filter_by(id=id)\
                 .first()
    if not item:
        return abort(404)
    return item


@app.route('/', methods=['GET'])
def health():
    return jsonify({'api': 'ok'}), 200


@app.route('/people', methods=['GET'])
def get_all():
    people = People.query.all()
    return jsonify({
        'list': [x.to_json(as_dict=True) for x in people]
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

    db.session.add(item)
    db.session.commit()

    id = item.id

    return jsonify({
        'id': id,
        'resource': f'/people/{id}'
    }), 201

@app.route('/people/<string:user_id>', methods=['GET'])
def get_item(user_id):
    item = get_by_id(user_id)
    return jsonify(item.to_json(as_dict=True)), 200

@app.route('/people/<string:user_id>', methods=['PATCH'])
def update_item(user_id):
    item = get_by_id(user_id)

    name = request.json.get('name')
    if name:
        item.name = name

    age = request.json.get('age')
    if age:
        item.age = age

    db.session.add(item)
    db.session.commit()
    return jsonify(''), 200

@app.route('/people/<string:user_id>', methods=['DELETE'])
def delete_item(user_id):
    item = get_by_id(user_id)
    db.session.delete(item)
    db.session.commit()

    return jsonify(''), 204