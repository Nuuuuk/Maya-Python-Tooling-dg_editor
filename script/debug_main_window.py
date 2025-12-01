import importlib as imp
from dg_editor import ui__main_window, reloader

# reload
imp.reload(reloader)

win = ui__main_window.new()