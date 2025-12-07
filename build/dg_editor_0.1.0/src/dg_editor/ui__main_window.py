# for py2
from __future__ import unicode_literals, print_function

import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance

from . import config
from . import ui_nodes as un
from . import ui_connect as uc
from . import ui_rename as ur
from . import ui_settings as us
from . import settings

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
        self.setWindowTitle("Dependency Graph Editor {}".format(config.VERSION))

        # create an empty vertical layout
        self.main_layout = layout = QVBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)

        # create widget
        self.tab = tab = QTabWidget(self)
        tab.addTab(un.new(), "Node Create")
        tab.addTab(uc.new(), "Connection")
        tab.addTab(ur.new(), "Rename")
        tab.addTab(us.new(), "Settings")

        # add widget to layout
        layout.addWidget(tab)

        # apply font size
        self.set_font_size()

    def set_font_size(self):
        font_size = settings.get_font_size()
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)


def new():
    win = DGEditorWindow()
    win.show()

    # only when DEBUG, fire and forget, shouldn't depend on return
    if config.DEBUG:
        return win