"""
a dialog from Create Widget in Node Tab to generate expression
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtWidgets import *

from . import nodes_create_dialog
from .widgets import BaseDialog
from . import settings

class ExpGenDialog(BaseDialog):
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

        settings.bind_lineedit(self.name_line_edit, 'node_create_name', 'prefix_{id}_suffix')
        settings.bind_lineedit(self.type_line_edit, 'node_create_type', 'joint')
        settings.bind_spinbox(self.node_num, 'node_create_num', 10)

        self.main_layout.addWidget(QLabel("Name: "))
        self.main_layout.addWidget(self.name_line_edit)
        self.main_layout.addWidget(QLabel("Type: "))
        self.main_layout.addWidget(self.type_line_edit)
        self.main_layout.addWidget(QLabel("Node Num: "))
        self.main_layout.addWidget(self.node_num)
        self.main_layout.addWidget(self.gen_bn)

    def gen(self):
        num = self.node_num.value()
        exp = self.name_line_edit.text()
        type_ = self.type_line_edit.text()
        values = [{"id": i} for i in range(num)]

        self.results = [(n, type_) for n in nodes_create_dialog.parse(exp, values)]

        # close dialog and return true after Generation
        self.accept()

def show(parent=None):
    return ExpGenDialog.show_ui(parent)