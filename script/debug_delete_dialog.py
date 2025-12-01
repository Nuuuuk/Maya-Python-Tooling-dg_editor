# for py2
from __future__ import unicode_literals, print_function

import importlib as imp
from dg_editor import reloader, ui_nodes_delete_dialog

# reload
imp.reload(reloader)

print(ui_nodes_delete_dialog.show())