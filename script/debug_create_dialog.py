import importlib as imp
import init
import create_dialog

# reload
imp.reload(init)

win = create_dialog.exec_()