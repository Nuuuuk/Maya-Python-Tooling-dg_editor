# for py2
from __future__ import unicode_literals, print_function

import config
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class WidgetConnections(QWidget):
    def __init__(self, parent=None):
        super(WidgetConnections, self).__init__(parent)

        # create an empty vertical layout
        self.widget_layout = layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # add label
        layout.addWidget(QLabel(text="Connections", parent=None))

        #apply layout to widget
        self.setLayout(layout)

def new():
    return WidgetConnections()