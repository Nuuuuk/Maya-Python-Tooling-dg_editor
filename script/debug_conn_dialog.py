import importlib as imp
import init
import conn_dialog

# reload
imp.reload(init)

win = conn_dialog.exec_()