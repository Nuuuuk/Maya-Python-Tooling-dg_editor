"""
dialog from Connection Tab to match by regex
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtWidgets import *

import conn_dialog_parser

class ConnMatchDialog(QDialog):
    def __init__(self, parent=None):
        self.name_types = []
        super(ConnMatchDialog, self).__init__(parent)
        self.setWindowTitle("Regular Expression Match")
        self.main_layout = QHBoxLayout(self)

        self.name_line_edit = QLineEdit(self)
        self.match_bn = QPushButton("Match")
        self.match_bn.clicked.connect(self.gen)


        self.main_layout.addWidget(QLabel("Regex: "))
        self.main_layout.addWidget(self.name_line_edit)
        self.main_layout.addWidget(self.match_bn)

    def gen(self):
        self.names = list(conn_dialog_parser.get_matched_nodes(self.name_line_edit.text()))

        # close dialog after generation
        self.close()

def exec_(parent=None):
    dia = ConnMatchDialog(parent)
    dia.exec_()
    return dia.names