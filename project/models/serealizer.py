from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from ..models.model import User

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User 
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    