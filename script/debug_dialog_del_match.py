import importlib as imp
import init
import dialog_del_match

# reload
imp.reload(init)

win = dialog_del_match.exec_()