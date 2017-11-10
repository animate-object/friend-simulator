from marshmallow import Schema, fields
from marshmallow.validate import OneOf

from src.type_chart import INTERESTS


class AttackSchema(Schema):
    name = fields.String(required=True)
    types = fields.List(fields.String(validate=OneOf(INTERESTS), required=True))
    base_damage = fields.Integer(required=True)
    cast = fields.List(fields.String())
    effects = fields.List(fields.String())