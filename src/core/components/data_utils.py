import json
import os

from src.core.components.attack import Attack

from paths import DATA_DIR
from src.core.components.char import Character


def character_from_json(file_name, data_dir=None):
    file_name = file_name + '.json' if not file_name.endswith('.json') else file_name
    if data_dir:
        path = os.path.join(data_dir, file_name)
    else:
        path = os.path.join(DATA_DIR, 'characters', file_name)

    with open(path, 'r') as data_in:
        raw_data = json.loads(
            data_in.read()
        )

    attacks = [attack_from_json(attack + '.json') for attack in raw_data.get('attacks', [])]

    return Character(
        raw_data.get('name'), raw_data.get('interests'), attacks, raw_data.get('health'),
        raw_data.get('pn'), raw_data.get('ppn'), raw_data.get('opn'),
        **raw_data.get('other', {})
    )

def attack_from_json(file_name, data_dir=None):
    file_name = file_name + '.json' if not file_name.endswith('.json') else file_name
    if data_dir:
        path = os.path.join(data_dir, file_name)
    else:
        path = os.path.join(DATA_DIR, 'attacks', file_name)

    with open(path, 'r') as data_in:
        raw_data = json.loads(
            data_in.read()
        )

    return Attack(
        raw_data.get('types'), raw_data.get('base_damage'), raw_data.get('name'), raw_data.get('effects'),
        raw_data.get('cast'), **raw_data.get('other', {})
    )
