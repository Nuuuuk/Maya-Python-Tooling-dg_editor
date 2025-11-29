"""
Rename Tab
"""

# for py2
from __future__ import unicode_literals, print_function

import config
import sys
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class BaseWidget(QWidget):
    def __init__(self, parent=None):
        super(BaseWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

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
        self.body_layout = QHBoxLayout()
        label = QLabel("Prefix:")
        label.setAlignment(Qt.AlignRight)
        label.setFixedWidth(80)
        self.text_input = QLineEdit()
        self.exec_btn = QPushButton("Add")
        self.body_layout.addWidget(label)
        self.body_layout.addWidget(self.text_input)
        self.body_layout.addWidget(self.exec_btn)

        self.main_layout.addWidget(QLabel("Add Prefix"))
        self.main_layout.addLayout(self.body_layout)


class WidgetReplace(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetReplace, self).__init__(parent)
        self.search_layout = search_layout = QHBoxLayout()
        self.main_layout.addWidget(QLabel("Search and Replace"))

        self.main_layout.addStretch()


class WidgetRename(QWidget):
    def __init__(self, parent=None):
        super(WidgetRename, self).__init__(parent)

        # create an empty vertical layout
        self.widget_layout = layout = QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)

        self.widget_a = widget_a = WidgetPrefix(self)
        self.widget_b = widget_b = WidgetReplace(self)

        layout.addWidget(widget_a)
        layout.addWidget(widget_b)

        #apply layout to widget
        self.setLayout(layout)

def new():
    return WidgetRename()