"""
Node Tab
"""

# for py2
from __future__ import unicode_literals, print_function

import config
import sys
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import maya.cmds as cmds

import exp_parser_node_create
import dialog_exp_gen

class BaseWidget(QWidget):
    def __init__(self, parent=None):
        super(BaseWidget, self).__init__(parent)

    def create_node(self):
        exp_text = self.name_text.toPlainText()
        for name, type in exp_parser_node_create.Exp(exp_text):
            cmds.createNode(type, name=name)

    # override virtual func, this will auto execute when needed
    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(62,62,62)))
        p.drawRect(self.rect())
        p.end()

# upper layout to create nodes
class WidgetCreate(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetCreate, self).__init__(parent)

        # body_layout
        self.name_text = QTextEdit()
        self.create_exp_btn = QPushButton("Create by Exp")
        self.create_exp_btn.setFixedWidth(170)

        self.create_exp_btn.clicked.connect(self.create_exp)

        self.create_exp_btn_layout = QVBoxLayout()
        self.create_exp_btn_layout.addWidget(self.create_exp_btn)
        self.create_exp_btn_layout.addStretch()
        self.body_layout = body_layout = QHBoxLayout()
        body_layout.addWidget(self.name_text)
        body_layout.addLayout(self.create_exp_btn_layout)

        # main_layout
        self.create_btn = QPushButton("Create")
        self.create_btn.clicked.connect(self.create_node)

        self.main_layout = main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel(text="Create: ", parent=None))
        main_layout.addLayout(body_layout)
        main_layout.addWidget(self.create_btn)

        # apply layout to self
        self.setLayout(main_layout)

    def create_exp(self):
        names = dialog_exp_gen.exec_()
        self.name_text.setText("\n".join(("{}: {}".format(n,t) for n,t in names)))

# lower layout to delete nodes
class WidgetDelete(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetDelete, self).__init__(parent)

        # body_layout
        self.name_text = QTextEdit()
        self.match_exp_btn = QPushButton("Match by Regular Exp")
        self.match_exp_btn.setFixedWidth(170)

        self.match_exp_btn_layout = QVBoxLayout()
        self.match_exp_btn_layout.addWidget(self.match_exp_btn)
        self.match_exp_btn_layout.addStretch()
        self.body_layout = body_layout = QHBoxLayout()
        body_layout.addWidget(self.name_text)
        body_layout.addLayout(self.match_exp_btn_layout)

        # main_layout
        self.delete_btn = QPushButton("Delete")

        self.main_layout = main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel(text="Delete: ", parent=None))
        main_layout.addLayout(body_layout)
        main_layout.addWidget(self.delete_btn)

        # apply layout to self
        self.setLayout(main_layout)

class WidgetNodes(QWidget):
    def __init__(self, parent=None):
        super(WidgetNodes, self).__init__(parent)

        # create an empty vertical layout
        self.widget_layout = layout = QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)

        self.widget_a = widget_a = WidgetCreate(self)
        self.widget_b = widget_b = WidgetDelete(self)

        layout.addWidget(widget_a)
        layout.addWidget(widget_b)

        #apply layout to widget
        self.setLayout(layout)

def new():
    return WidgetNodes()