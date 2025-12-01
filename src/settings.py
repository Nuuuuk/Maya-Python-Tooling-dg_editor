# for py2
from __future__ import unicode_literals, print_function

import json, os
import codecs
import config

JSON_PATH = os.path.join(config.PATH, "settings.json")

def _get_json():
    if not os.path.isfile(JSON_PATH):
        _save_json(dict())
    with codecs.open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_json(data):
    with codecs.open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f)


def set(key, val):
    data = _get_json()
    data[key] = val
    _save_json(data)


def get(key, default):
    data = _get_json()
    return data.get(key, default)


# default settings
def get_font_size():
    return get('font_size', 10)

def get_undo_check():
    return get('undo_check', True)