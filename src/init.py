# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

# import modules needed
import config

import nodes_create, nodes_delete_dialog, nodes_connect_dialog, rename

import ui_nodes_create_dialog, ui_nodes_delete_dialog, ui_connect_dialog

import ui_nodes, ui_connect, ui_rename, ui_settings

import ui__main_window


# reload config at first
imp.reload(config)

modules = [
    nodes_create,
    nodes_delete_dialog,
    nodes_connect_dialog,
    rename,

    ui_nodes_create_dialog,
    ui_nodes_delete_dialog,
    ui_connect_dialog,

    ui_nodes,
    ui_connect,
    ui_rename,
    ui_settings,

    ui__main_window,
]

if config.DEBUG:
    # reload everything
    for m in modules:
        imp.reload(m)

else:
    pass
