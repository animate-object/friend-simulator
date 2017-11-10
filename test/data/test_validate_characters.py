"""
Validate the data in the attack files.
"""
import json
import os

from marshmallow import ValidationError
from pytest import fail, mark

from paths import DATA_DIR
from test.data.data_models import CharacterSchema


def _gen_character_paths():
    character_dir = os.path.join(DATA_DIR, 'characters')

    character_walker = os.walk(character_dir)

    for _path, _, files in character_walker:
        for file_path in (os.path.join(_path, file) for file in files):
            yield file_path


@mark.parametrize('file_path', _gen_character_paths())
def test_validate_attacks(file_path):
    with open(file_path, 'r') as fin:
        try:
            CharacterSchema(strict=True).validate(json.load(fin))
        except ValidationError as v:
            fail("Character definition {} is invalid:\n{}".format(file_path, v))
