# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)

        if not parent:
            # Maya main window's pointer
            maya_main_ptr = int(MQtUtil.mainWindow())
            # Maya main window
            maya_main = wrapInstance(maya_main_ptr, QWidget)
            # Maya as parent
            self.setParent(maya_main)

        # set as floating window, otherwise it's onto maya main window
        self.setWindowFlag(Qt.Window)