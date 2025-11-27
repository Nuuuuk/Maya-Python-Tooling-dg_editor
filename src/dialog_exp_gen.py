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

        self.node_num = QSpinBox(self)
        self.node_num.setRange(1, 999)
        self.name_line_edit = QLineEdit(self)
        self.type_line_edit = QLineEdit(self)
        self.gen_bn = QPushButton("Generate")
        self.gen_bn.clicked.connect(self.gen)


        self.main_layout.addWidget(QLabel("Name: "))
        self.main_layout.addWidget(self.name_line_edit)
        self.main_layout.addWidget(QLabel("Type: "))
        self.main_layout.addWidget(self.type_line_edit)
        self.main_layout.addWidget(QLabel("Node Num: "))
        self.main_layout.addWidget(self.node_num)
        self.main_layout.addWidget(self.gen_bn)


def exec_(parent=None):
    dia = ExpGenDialog(parent)
    dia.exec_()