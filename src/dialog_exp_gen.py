"""
a dialog in Node Tab to generate expression
"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class ExpGenDialog(QDialog):
    def __init__(self, parent=None):
        super(ExpGenDialog, self).__init__(parent)

def new(parent=None):
    dialog = ExpGenDialog(parent)
    dialog.exec_()
    return dialog