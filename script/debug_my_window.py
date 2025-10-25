import importlib as imp
import init
import my_window

# reload
imp.reload(init)

win = my_window.MyWindow()
win.show()