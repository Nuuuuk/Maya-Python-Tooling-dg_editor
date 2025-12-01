"""
Node Tab
"""

# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import maya.cmds as cmds

from widgets import BaseWidget
import nodes_create
import ui_nodes_create_dialog
import ui_nodes_delete_dialog


# upper layout to create nodes
class WidgetCreate(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetCreate, self).__init__(parent)

        self.create_btn = QPushButton("Create")
        self.create_btn.clicked.connect(self.create_node)

        main_layout = self.main_layout
        self.add_header("Create: ")

        body_layout, self.name_text, self.create_exp_btn = (
            self.add_text_btn_block(
                btn_text="Create by Exp",
                btn_connect=self.create_dialog
            )
        )

        main_layout.addWidget(self.create_btn)

    def create_node(self):
        exp_text = self.name_text.toPlainText()
        for name, type in nodes_create.parser(exp_text):
            cmds.createNode(type, name=name)

    def create_dialog(self):
        names = ui_nodes_create_dialog.exec_(self)
        if not names:
            cmds.warning("Operation cancelled")
            return
        self.name_text.setPlainText("\n".join(("{}: {}".format(n,t) for n,t in names)))

# lower layout to delete nodes
class WidgetDelete(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetDelete, self).__init__(parent)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_node)

        main_layout = self.main_layout
        self.add_header("Delete: ")

        body_layout, self.name_text, self.match_exp_btn = (
            self.add_text_btn_block(
                btn_text="Match by Regex",
                btn_connect=self.delete_dialog
            )
        )

        main_layout.addWidget(self.delete_btn)

    def delete_node(self):
        node_names = self.name_text.toPlainText().splitlines()
        if len(node_names) < 1: return
        cmds.delete(node_names)

    def delete_dialog(self):
        names = ui_nodes_delete_dialog.exec_(self)
        if not names:
            cmds.warning("Operation cancelled")
            return
        self.name_text.setPlainText("\n".join(names))


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