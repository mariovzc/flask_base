import json
import datetime
import decimal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import DOUBLE, SMALLINT
from sqlalchemy.types import DECIMAL
from sqlalchemy import text, PrimaryKeyConstraint

db = SQLAlchemy()


class People(db.Model):
    __tablename__ = 'people'

    id = db.Column('id',
                   db.Integer,
                   primary_key=True,
                   nullable=False)
    name = db.Column('name',
                     db.String(100),
                     nullable=False)


    age = db.Column('age',
                    db.Integer)

    def to_json(self, as_dict=False):
        output = {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

        json_output = json.dumps(output)
        if as_dict:
            return json.loads(json_output)
        return json_output
