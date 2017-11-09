"""
Validate the data in the attack files.
"""
import json
import os

from paths import DATA_DIR


def test_validate_attacks():
    attacks_dir = os.path.join(DATA_DIR, 'attacks')

    attacks_walker = os.walk(attacks_dir)

    for _path, _, files in attacks_walker:
        for file_path in (os.path.join(_path, file) for file in files):
            _validate_attack(file_path)

def _validate_attack(file_path):
    with open(file_path, 'r') as fin:
        attack_dict = json.load(fin)
        import pdb; pdb.set_trace()