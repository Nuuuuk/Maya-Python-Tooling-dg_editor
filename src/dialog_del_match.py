"""
a dialog from Delete Widget in Node Tab to match by regex
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class DelMatchDialog(QDialog):
    def __init__(self, parent=None):
        self.name_types = []
        super(DelMatchDialog, self).__init__(parent)
        self.setWindowTitle("Regular Expression Match")
        self.main_layout = QHBoxLayout(self)

        self.name_line_edit = QLineEdit(self)
        self.match_bn = QPushButton("Match")
        self.match_bn.clicked.connect(self.gen)


        self.main_layout.addWidget(QLabel("Regex: "))
        self.main_layout.addWidget(self.name_line_edit)
        self.main_layout.addWidget(self.match_bn)

    def gen(self):
        self.names = []

        # close dialog after generation
        self.close()

def exec_(parent=None):
    dia = DelMatchDialog(parent)
    dia.exec_()
    return dia.name_types