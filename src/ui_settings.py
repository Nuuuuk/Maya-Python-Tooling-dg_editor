"""
Settings Tab
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from widgets import BaseWidget
import settings

class FontSizeWidget(BaseWidget):
    def __init__(self, parent=None):
        super(FontSizeWidget, self).__init__(parent)
        self.font_size_input = QSpinBox()
        self.font_size_input.setRange(5, 15)

        self.font_size_input.setValue(self.get_font_size())
        self.font_size_input.valueChanged.connect(lambda *args: self.set_font_size())

        self.add_input_row("Font Size", self.font_size_input, False)

    def get_font_size(self):
        return settings.get_font_size()

    def set_font_size(self):
        settings.set("font_size", self.font_size_input.value())


class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super(SettingsWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.font_size_widget = FontSizeWidget(self)

        self.main_layout.addWidget(self.font_size_widget)
        self.main_layout.addStretch()


def new():
    return SettingsWidget()