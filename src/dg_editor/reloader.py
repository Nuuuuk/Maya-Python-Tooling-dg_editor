# for py2
from __future__ import unicode_literals, print_function

import sys

if sys.version_info[0] >= 3:
    import importlib
    def _reload(m):
        importlib.reload(m)
else:
    def _reload(m):
        reload(m)

from . import config
# reload config at first
_reload(config)

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
    print("--- Reloading DG Editor Modules ---")
    for m in modules:
        try:
            _reload(m)
        except Exception as e:
            print("Failed to reload {}: {}".format(m, e))

else:
    pass
