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

import maya.cmds as cmds


class WidgetRename(QWidget):
    def __init__(self, parent=None):
        super(WidgetRename, self).__init__(parent)

        # create an empty vertical layout
        self.widget_layout = layout = QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)

        # self.widget_a = widget_a = WidgetCreate(self)
        # self.widget_b = widget_b = WidgetDelete(self)
        #
        # layout.addWidget(widget_a)
        # layout.addWidget(widget_b)

        #apply layout to widget
        self.setLayout(layout)

def new():
    return WidgetRename()