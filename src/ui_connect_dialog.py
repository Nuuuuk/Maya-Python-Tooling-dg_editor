"""
dialog from Connection Tab to match by regex
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtWidgets import *

import connect_dialog
from widgets import BaseDialog

class ConnMatchDialog(BaseDialog):
    def __init__(self, parent=None):
        super(ConnMatchDialog, self).__init__(parent)
        self.setWindowTitle("Regular Expression Match")
        self.main_layout = QHBoxLayout(self)

        self.name_line_edit = QLineEdit(self)
        self.match_bn = QPushButton("Match")
        self.match_bn.clicked.connect(self.match)


        self.main_layout.addWidget(QLabel("Regex: "))
        self.main_layout.addWidget(self.name_line_edit)
        self.main_layout.addWidget(self.match_bn)

    def match(self):
        self.results = list(connect_dialog.get_matched_nodes(self.name_line_edit.text()))

        # close dialog after Match
        self.accept()

def show(parent=None):
    return ConnMatchDialog.show_ui(parent)
# def exec_(parent=None):
#     dia = ConnMatchDialog(parent)
#     dia.exec_()
#     return dia.results