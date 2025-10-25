# for py2
from __future__ import unicode_literals, print_function

import config
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance

if sys.version_info.major >= 3:
    long = int # shim

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)

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

def new():
    win = MyWindow()
    win.show()

    # only when DEBUG, fire and forget, shouldn't depend on return
    if config.DEBUG:
        return win