# for py2
from __future__ import unicode_literals, print_function

import importlib as imp
from dg_editor import ui_nodes_create_dialog, reloader

# reload
imp.reload(reloader)

print(ui_nodes_create_dialog.show())