import importlib as imp
import init
import ui__main_window

# reload
imp.reload(init)

win = ui__main_window.new()