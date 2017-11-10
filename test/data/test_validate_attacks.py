"""
Validate the data in the attack files.
"""
import json
import os

from marshmallow import ValidationError
from pytest import fail, mark

from paths import DATA_DIR
from test.data.data_models import AttackSchema


def _gen_attack_paths():
    attacks_dir = os.path.join(DATA_DIR, 'attacks')

    attacks_walker = os.walk(attacks_dir)

    for _path, _, files in attacks_walker:
        for file_path in (os.path.join(_path, file) for file in files):
            yield file_path


@mark.parametrize('file_path', _gen_attack_paths())
def test_validate_attacks(file_path):
    with open(file_path, 'r') as fin:
        try:
            AttackSchema(strict=True).validate(json.load(fin))
        except ValidationError as v:
            fail("Attack definition {} is invalid:\n{}".format(file_path, v))
