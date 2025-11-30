"""
Rename Tab
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import rename

class BaseWidget(QWidget):
    def __init__(self, parent=None):
        super(BaseWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

    def add_header(self, text):
        """add top header"""
        self.main_layout.addWidget(QLabel(text))

    def add_row(self, text, widget=None):
        """
        create a [Label (80px, Right)] + [Widget] horizontal layout
        if widget is None, create a QLineEdit
        """
        h_layout = QHBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignRight)
        label.setFixedWidth(80)

        if widget is None: widget = QLineEdit()

        h_layout.addWidget(label)
        h_layout.addWidget(widget)

        self.main_layout.addLayout(h_layout)

        return h_layout, widget

    # a faint background to distinguish two widgets
    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(62,62,62)))
        p.drawRect(self.rect())
        p.end()


class WidgetPrefix(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetPrefix, self).__init__(parent)

        self.add_header("Add Prefix")
        body_layout, self.text_input = self.add_row("Prefix:")

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
        search_layout, self.search_input = self.add_row("Search:")
        replace_layout, self.replace_input = self.add_row("Replace:")
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