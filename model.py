import json
from datetime import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()

class People(db.Document):

    name = db.StringField(required=True)
    age = db.IntField(required=True)

    def to_json(self, as_dict=True):
        item = {
            'id': str(self.id),
            'name': self.name,
            'age': self.age
        }
        if as_dict:
            return item
        return json.dumps(item)