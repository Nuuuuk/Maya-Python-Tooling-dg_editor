# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

import config
# reload config at first
imp.reload(config)

# import modules needed
from . import widgets

from . import nodes_create, nodes_delete_dialog, connect_dialog, rename, settings

from . import ui_nodes_create_dialog, ui_nodes_delete_dialog, ui_connect_dialog

from . import ui_nodes, ui_connect, ui_rename, ui_settings

from . import ui__main_window


modules = [
    widgets,

    nodes_create,
    nodes_delete_dialog,
    connect_dialog,
    rename,
    settings,

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
