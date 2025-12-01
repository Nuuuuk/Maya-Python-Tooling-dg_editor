"""
Settings Tab
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtWidgets import *

from .widgets import BaseWidget
from . import settings


class UndoWidget(BaseWidget):
    def __init__(self, parent=None):
        super(UndoWidget, self).__init__(parent)
        self.undo_check = QCheckBox()

        self.undo_check.setChecked(self.get_undo_check())
        self.undo_check.toggled.connect(lambda *args: self.set_undo_check())

        self.add_input_row("Bulk Undo", self.undo_check, False)

    def get_undo_check(self):
        return settings.get_undo_check()

    def set_undo_check(self):
        settings.set("undo_check", self.undo_check.isChecked())


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
        self.undo_check_widget = UndoWidget(self)

        self.main_layout.addWidget(self.font_size_widget)
        self.main_layout.addWidget(self.undo_check_widget)
        self.main_layout.addStretch()


def new():
    return SettingsWidget()