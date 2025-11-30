# for py2
from __future__ import unicode_literals, print_function

import importlib as imp
import init
import ui_nodes_create_dialog

# reload
imp.reload(init)

print(ui_nodes_create_dialog.exec_())