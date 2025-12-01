# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import settings


class BaseWidget(QWidget):
    def __init__(self, parent=None):
        super(BaseWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

    def add_header(self, text):
        """add top header"""
        self.main_layout.addWidget(QLabel(text))

    def add_input_row(self, text, widget=None, stretch=True):
        """
        create a [Label (80px, Right)] + [Widget] horizontal layout
        if widget is None, create a QLineEdit
        """
        h_layout = QHBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignRight)
        label.setFixedWidth(100)

        if widget is None: widget = QLineEdit()

        h_layout.addWidget(label)
        h_layout.addWidget(widget)
        if not stretch:
            h_layout.addStretch(0)

        self.main_layout.addLayout(h_layout)

        return h_layout, widget

    def paintEvent(self, event):
        """
        a faint background to distinguish from other widgets
        """
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(62,62,62)))
        p.drawRect(self.rect())
        p.end()

    def add_text_btn_block(self, btn_text, btn_connect, widget=None):
        """
        create a [Widget] + [Button] horizontal layout
        if widget is None, create a QTextEdit
        """
        if widget is None: widget = QTextEdit()
        btn = QPushButton(btn_text)
        btn.setFixedWidth(170)

        btn.clicked.connect(btn_connect)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(btn)
        btn_layout.addStretch()

        body_layout = QHBoxLayout()
        body_layout.addWidget(widget)
        body_layout.addLayout(btn_layout)

        self.main_layout.addLayout(body_layout)

        return body_layout, widget, btn


class BaseDialog(QDialog):
    def __init__(self, parent=None):
        super(BaseDialog, self).__init__(parent)

        self.results = []
        self.apply_font()

    def apply_font(self):
        font_size = settings.get_font_size()
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    @classmethod
    def show_ui(cls, parent=None):
        """
        uniform entrance, replaces the outer exec_ function
        """
        dia = cls(parent)
        if dia.exec_():
            return dia.results
        return []