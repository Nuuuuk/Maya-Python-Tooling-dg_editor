# for py2
from __future__ import unicode_literals, print_function

import importlib as imp
from dg_editor import ui_connect_dialog, reloader

# reload
imp.reload(reloader)

print(ui_connect_dialog.show())