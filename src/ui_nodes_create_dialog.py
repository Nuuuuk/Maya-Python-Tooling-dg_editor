"""
a dialog from Create Widget in Node Tab to generate expression
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtWidgets import *
import nodes_create_dialog
import settings

class ExpGenDialog(QDialog):
    def __init__(self, parent=None):
        self.name_types = []
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

        # apply font size
        self.set_font_size()

    def set_font_size(self):
        font_size = settings.get('font_size')
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def gen(self):
        num = self.node_num.value()
        exp = self.name_line_edit.text()
        type_ = self.type_line_edit.text()
        values = [{"id": i} for i in range(num)]

        self.name_types = [(n, type_) for n in nodes_create_dialog.parse(exp, values)]

        # close dialog after generation
        self.close()

def exec_(parent=None):
    dia = ExpGenDialog(parent)
    dia.exec_()
    return dia.name_types