"""
Settings Tab
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

class FontSizeWidget(QWidget):
    def __init__(self, parent=None):
        super(FontSizeWidget, self).__init__(parent)
        self.main_layout = QHBoxLayout(self)
        self.font_size_intput = QSpinBox()
        self.font_size_intput.setRange(5, 15)

        self.main_layout.addWidget(QLabel("Font Size"))
        self.main_layout.addWidget(self.font_size_intput)
        self.main_layout.addStretch()

    # a faint background to distinguish two widgets
    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(62,62,62)))
        p.drawRect(self.rect())
        p.end()


class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.font_size_widget = FontSizeWidget(self)

        self.main_layout.addWidget(self.font_size_widget)
        self.main_layout.addStretch()


def new():
    return SettingsWidget()