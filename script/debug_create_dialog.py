import importlib as imp
import init
import ui_nodes_create_dialog

# reload
imp.reload(init)

win = ui_nodes_create_dialog.exec_()