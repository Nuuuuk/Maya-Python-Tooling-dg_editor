"""
Rename Tab
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from widgets import BaseWidget
import rename


class WidgetPrefix(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetPrefix, self).__init__(parent)

        self.add_header("Add Prefix")
        body_layout, self.text_input = self.add_input_row("Prefix:")

        # button at the end
        self.add_btn = QPushButton("Add")
        self.add_btn.clicked.connect(self.add_name_prefix)

        body_layout.addWidget(self.add_btn)

    def add_name_prefix(self):
        rename.add_name_prefix(self.text_input.text())

class WidgetReplace(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetReplace, self).__init__(parent)

        self.btn_layout = btn_layout = QHBoxLayout()

        self.normal_btn = QPushButton("Normal Replace")
        self.normal_btn.clicked.connect(self.replace)

        self.regex_btn = QPushButton("Regex Replace")
        self.regex_btn.clicked.connect(self.regex_replace)

        btn_layout.addWidget(self.normal_btn)
        btn_layout.addWidget(self.regex_btn)

        self.add_header("Search and Replace")
        search_layout, self.search_input = self.add_input_row("Search:")
        replace_layout, self.replace_input = self.add_input_row("Replace:")
        self.main_layout.addLayout(self.btn_layout)

        self.main_layout.addStretch()

    def replace(self):
        rename.search_n_replace(self.search_input.text(), self.replace_input.text())

    def regex_replace(self):
        rename.regex_search_n_replace(self.search_input.text(), self.replace_input.text())


class WidgetRename(QWidget):
    def __init__(self, parent=None):
        super(WidgetRename, self).__init__(parent)

        # create an empty vertical layout
        self.widget_layout = layout = QVBoxLayout(self)
        # layout.setContentsMargins(0, 0, 0, 0)

        self.widget_a = widget_a = WidgetPrefix(self)
        self.widget_b = widget_b = WidgetReplace(self)

        layout.addWidget(widget_a)
        layout.addWidget(widget_b)


def new():
    return WidgetRename()