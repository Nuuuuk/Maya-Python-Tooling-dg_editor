import importlib as imp
import init
import delete_dialog

# reload
imp.reload(init)

win = delete_dialog.exec_()