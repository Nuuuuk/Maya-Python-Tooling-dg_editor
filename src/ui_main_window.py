# for py2
from __future__ import unicode_literals, print_function

import config
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance

import ui_tab_nodes as utn
import ui_tab_connections as utc

if sys.version_info.major >= 3:
    long = int # shim

class DGEditorWindow(QWidget):
    def __init__(self, parent=None):
        super(DGEditorWindow, self).__init__(parent=parent)

        if not parent:
            # Maya main window's pointer
            if sys.version_info.major >= 3:
                maya_main_ptr = int(MQtUtil.mainWindow())
            else:
                maya_main_ptr = long(MQtUtil.mainWindow())

            # Maya main window
            maya_main = wrapInstance(maya_main_ptr, QWidget)
            # Maya as parent
            self.setParent(maya_main)

        # set as floating window, otherwise it's onto maya main window
        self.setWindowFlags(Qt.Window)

        # add title
        self.setWindowTitle("dg editor {}".format(config.VERSION))

        # create an empty vertical layout
        self.main_layout = layout = QVBoxLayout()
        layout.setContentsMargins(1, 1, 1, 1)

        # create widget
        self.tab = tab = QTabWidget(self)
        tab.addTab(utn.new(), "Node")
        tab.addTab(utc.new(), "Connection")
        tab.addTab(QLabel(text="Settings", parent=None), "Settings")

        # add widget to layout
        layout.addWidget(tab)

        # apply layout to widget
        self.setLayout(layout)

def new():
    win = DGEditorWindow()
    win.show()

    # only when DEBUG, fire and forget, shouldn't depend on return
    if config.DEBUG:
        return win