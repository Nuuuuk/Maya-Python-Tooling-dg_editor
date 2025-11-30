import importlib as imp
import init
import ui_connect_dialog

# reload
imp.reload(init)

win = ui_connect_dialog.exec_()