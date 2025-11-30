"""
a dialog from Delete Widget in Node Tab to match by regex
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtWidgets import *

import nodes_delete_dialog
import settings

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

        # apply font size
        self.set_font_size()

    def set_font_size(self):
        font_size = settings.get('font_size')
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def gen(self):
        self.names = list(nodes_delete_dialog.get_matched_nodes(self.name_line_edit.text()))

        # close dialog after generation
        self.close()

def exec_(parent=None):
    dia = DelMatchDialog(parent)
    dia.exec_()
    return dia.names