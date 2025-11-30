import importlib as imp
import init
import ui_nodes_delete_dialog

# reload
imp.reload(init)

win = ui_nodes_delete_dialog.exec_()