# for py2
from __future__ import unicode_literals, print_function

import config
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class WidgetFuncSelect(QWidget):
    Connect, Disconnect = range(2)
    ConnectText = "Connect"
    DisconnectText = "Disconnect"

    def __init__(self, parent=None):
        super(WidgetFuncSelect, self).__init__(parent)
        self.main_layout = layout = QHBoxLayout()
        self.func_combo = QComboBox()
        self.func_combo.addItem(self.ConnectText)
        self.func_combo.addItem(self.DisconnectText)

        layout.addWidget(QLabel('Function:'))
        layout.addWidget(self.func_combo)
        layout.addStretch(0)

        self.setLayout(layout)

    def func(self):
        if self.func_combo.currentText() == self.ConnectText:
            return self.Connect
        else:
            return self.Disconnect

class WidgetConnections(QWidget):
    def __init__(self, parent=None):
        super(WidgetConnections, self).__init__(parent)

        # create an empty vertical layout
        self.main_layout = layout = QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)
        self.widget_func_select = widget_func_select = WidgetFuncSelect(self)
        layout.addWidget(widget_func_select)

        #apply layout to widget
        self.setLayout(layout)

def new():
    return WidgetConnections()