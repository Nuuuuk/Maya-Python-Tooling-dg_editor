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

        settings.bind_checkbox(self.undo_check, "settings_undo_check", True)

        self.add_input_row("Bulk Undo", self.undo_check, False)


class FontSizeWidget(BaseWidget):
    def __init__(self, parent=None):
        super(FontSizeWidget, self).__init__(parent)
        self.font_size_input = QSpinBox()
        self.font_size_input.setRange(5, 15)

        settings.bind_spinbox(self.font_size_input, "settings_font_size", 10)

        self.add_input_row("Font Size", self.font_size_input, False)


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