# for py2
from __future__ import unicode_literals, print_function

import config
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
import maya.cmds as cmds
import conn_dialog

class WidgetFuncSelect(QWidget):
    Connect, Disconnect = range(2)
    ConnectText = "Connect"
    DisconnectText = "Disconnect"

    def __init__(self, parent=None):
        super(WidgetFuncSelect, self).__init__(parent)
        self.func_combo = QComboBox()
        self.func_combo.addItem(self.ConnectText)
        self.func_combo.addItem(self.DisconnectText)

        self.main_layout = layout = QHBoxLayout()
        layout.addWidget(QLabel('Function:'))
        layout.addWidget(self.func_combo)
        layout.addStretch(0)

        self.setLayout(layout)

    def func(self):
        if self.func_combo.currentText() == self.ConnectText:
            return self.Connect
        else:
            return self.Disconnect

class MatchWidget(QWidget):
    def __init__(self, parent=None):
        super(MatchWidget, self).__init__(parent)
        self.text_box = QTextEdit()
        self.match_exp_btn = QPushButton("Match by Regex")
        self.match_exp_btn.setFixedWidth(170)

        self.match_exp_btn.clicked.connect(self.match)

        self.match_exp_btn_layout = QVBoxLayout()
        self.match_exp_btn_layout.addWidget(self.match_exp_btn)
        self.match_exp_btn_layout.addStretch()
        self.body_layout = body_layout = QHBoxLayout()
        body_layout.addWidget(self.text_box)
        body_layout.addLayout(self.match_exp_btn_layout)

        self.setLayout(body_layout)

    def match(self):
        names = conn_dialog.exec_()
        self.text_box.setPlainText("\n".join(names))

    def get_attrs(self):
        return self.text_box.toPlainText().splitlines()


class WidgetConnections(QWidget):
    def __init__(self, parent=None):
        super(WidgetConnections, self).__init__(parent)

        # create an empty vertical layout
        self.main_layout = layout = QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)
        self.widget_func_select = widget_func_select = WidgetFuncSelect(self)
        self.widget_match_out_attrs = MatchWidget(self)
        self.widget_match_in_attrs = MatchWidget(self)
        self.exec_btn = QPushButton("Execute")

        self.exec_btn.clicked.connect(self.execute)

        layout.addWidget(widget_func_select)
        layout.addWidget(QLabel('From Attributes:'))
        layout.addWidget(self.widget_match_out_attrs)
        layout.addWidget(QLabel('To Attributes:'))
        layout.addWidget(self.widget_match_in_attrs)
        layout.addWidget(self.exec_btn)

        #apply layout to widget
        self.setLayout(layout)

    def execute(self):
        out_attrs = self.widget_match_out_attrs.get_attrs()
        in_attrs = self.widget_match_in_attrs.get_attrs()
        if len(out_attrs) != len(in_attrs):
            raise ValueError("out_attrs and in_attrs must have same length")
        for o, i in zip(out_attrs, in_attrs):
            if self.widget_func_select.func() == WidgetFuncSelect.Connect:
                cmds.connectAttr(o, i)
            else:
                cmds.disconnectAttr(o, i)


def new():
    return WidgetConnections()