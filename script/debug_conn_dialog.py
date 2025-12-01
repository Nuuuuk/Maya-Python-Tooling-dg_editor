# for py2
from __future__ import unicode_literals, print_function

import importlib as imp
import init
import ui_connect_dialog

# reload
imp.reload(init)

print(ui_connect_dialog.exec_())