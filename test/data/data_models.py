import os
from marshmallow import Schema, fields, ValidationError, validates
from marshmallow.validate import OneOf

from paths import DATA_DIR
from src.type_chart import INTERESTS


dir_file_listing = (files for _, __, files in os.walk(os.path.join(DATA_DIR, 'attacks')))
all_attack_files = [file[:-5] for files in dir_file_listing for file in files]

class AttackSchema(Schema):
    name = fields.String(required=True)
    types = fields.List(fields.String(validate=OneOf(INTERESTS), required=True))
    base_damage = fields.Integer(required=True)
    cast = fields.List(fields.String())
    effects = fields.List(fields.String())


class CharacterSchema(Schema):
    name = fields.String(required=True)
    interests = fields.List(fields.String(validate=OneOf(INTERESTS)), required=True)
    attacks = fields.List(fields.String())
    health = fields.Integer()
    other = fields.Dict()

    @validates('attacks')
    def attack_exists(self, attacks):
        errors = []
        for attack in attacks:
            if not attack in all_attack_files:
                errors.append("Attack {} is not defined".format(attack))
        if errors:
            raise ValidationError(', '.join(errors))