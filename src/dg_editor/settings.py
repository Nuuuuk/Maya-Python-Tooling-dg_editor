# for py2
from __future__ import unicode_literals, print_function

import json, os
import codecs
from . import config

JSON_PATH = os.path.join(config.PATH, "settings.json")

def _get_json():
    if not os.path.isfile(JSON_PATH):
        _save_json(dict())
    with codecs.open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_json(data):
    with codecs.open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f)


def _set(key, val):
    data = _get_json()
    data[key] = val
    _save_json(data)


def _get(key, default):
    data = _get_json()
    return data.get(key, default)


# default settings
def get_font_size():
    return _get('font_size', 10)


def get_undo_check():
    return _get('undo_check', True)


# UI Binding Helpers
def bind_checkbox(widget, key, default=True):
    current_val = _get(key, default)
    widget.setChecked(bool(current_val))

    # toggled auto returns val
    widget.toggled.connect(lambda val: _set(key, val))


def bind_spinbox(widget, key, default=10):
    current_val = _get(key, default)

    # make sure it's number
    try:
        widget.setValue(float(current_val))
    except ValueError:
        widget.setValue(default)

    # valueChanged auto returns val
    widget.valueChanged.connect(lambda val: _set(key, val))


def bind_lineedit(widget, key, default=""):
    current_val = _get(key, default)
    widget.setText(str(current_val))

    # editingFinished doesnt return val
    widget.editingFinished.connect(lambda: _set(key, widget.text()))


def bind_combobox(widget, key, default=None):
    # if default is None then use current selected
    default = widget.currentText() if default is None else default

    current_val = str(_get(key, default))
    index = widget.findText(current_val)
    if index != -1:
        widget.setCurrentIndex(index)

    # currentTextChanged auto returns val
    widget.currentTextChanged.connect(lambda val: _set(key, val))