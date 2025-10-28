"""
a dialog in Node Tab to generate expression
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class ExpGenDialog(QDialog):
    def __init__(self, parent=None):
        super(ExpGenDialog, self).__init__(parent)
        self.setWindowTitle("Generate Expression")
        self.main_layout = QHBoxLayout(self)

        self.name_line_edit = QLineEdit(self)
        self.type_line_edit = QLineEdit(self)
        self.run_bn = QPushButton("Generate")

        self.main_layout.addWidget(QLabel("Name: "))
        self.main_layout.addWidget(self.name_line_edit)
        self.main_layout.addWidget(QLabel("Type: "))
        self.main_layout.addWidget(self.type_line_edit)
        self.main_layout.addWidget(self.run_bn)


def exec_(parent=None):
    dia = ExpGenDialog(parent)
    dia.exec_()