# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

# import modules needed
import config

import create_parser, delete_dialog_parser, conn_dialog_parser, rename_logics

import create_dialog, delete_dialog, conn_dialog

import ui_tab_nodes, ui_tab_connections, ui_tab_rename

import ui_main_window


# reload config at first
imp.reload(config)

modules = [
    create_parser,
    delete_dialog_parser,
    conn_dialog_parser,
    rename_logics,

    create_dialog,
    delete_dialog,
    conn_dialog,

    ui_tab_nodes,
    ui_tab_connections,
    ui_tab_rename,

    ui_main_window,
]

if config.DEBUG:
    # reload everything
    for m in modules:
        imp.reload(m)

else:
    pass
