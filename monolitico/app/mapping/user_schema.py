from app.models.user import User
from marshmallow import validate, fields, Schema, post_load

class UserSchema(Schema):
    id = fields.Integer(dump_only = True)
    name = fields.String(required=True)
    dni = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())
    gender = fields.String(required=False)
    address = fields.String(required=False)
    phone = fields.String(required=True)
    data = fields.Dict(required=False)
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)