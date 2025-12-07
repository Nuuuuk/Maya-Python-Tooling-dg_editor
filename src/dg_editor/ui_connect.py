# for py2
from __future__ import unicode_literals, print_function

from PySide2.QtWidgets import *
import maya.cmds as cmds

from .widgets import BaseWidget
from . import ui_connect_dialog
from .utils import undo_block
from . import settings

class WidgetFuncSelect(BaseWidget):
    Connect, Disconnect, MatrixConnect = range(3)
    ConnectText = "Connect"
    DisconnectText = "Disconnect"
    MatrixConnectText = "Matrix Connect"

    def __init__(self, parent=None):
        super(WidgetFuncSelect, self).__init__(parent)

        self.func_combo = QComboBox()
        self.func_combo.addItem(self.ConnectText)
        self.func_combo.addItem(self.MatrixConnectText)
        self.func_combo.addItem(self.DisconnectText)

        settings.bind_combobox(self.func_combo, 'conn_operation', 'Connect')

        self.add_input_row('Operation', self.func_combo, False)

    def func(self):
        text = self.func_combo.currentText()
        if text == self.ConnectText:
            return self.Connect
        elif text == self.MatrixConnectText:
            return self.MatrixConnect
        else:
            return self.Disconnect

class MatchWidget(BaseWidget):
    def __init__(self, parent=None):
        super(MatchWidget, self).__init__(parent)

        _, self.text_box, self.match_exp_btn = self.add_text_btn_block(
            btn_text="Match by Regex",
            btn_connect=self.match
        )

    def match(self):
        names = ui_connect_dialog.show(self)
        if not names:
            cmds.warning("Operation cancelled")
            return
        self.text_box.setPlainText("\n".join(names))

    def get_attrs(self):
        return self.text_box.toPlainText().splitlines()


class WidgetConnections(BaseWidget):
    def __init__(self, parent=None):
        super(WidgetConnections, self).__init__(parent)

        layout = self.main_layout
        # layout.setContentsMargins(0, 0, 0, 0)
        self.widget_func_select = widget_func_select = WidgetFuncSelect(self)
        self.widget_match_out_attrs = MatchWidget(self)
        self.widget_match_in_attrs = MatchWidget(self)
        self.exec_btn = QPushButton("Execute")

        self.exec_btn.clicked.connect(self.execute)

        layout.addWidget(widget_func_select)
        self.add_header('From Attributes:')
        layout.addWidget(self.widget_match_out_attrs)
        self.add_header('To Attributes:')
        layout.addWidget(self.widget_match_in_attrs)
        layout.addWidget(self.exec_btn)

    @undo_block
    def execute(self):
        out_attrs = self.widget_match_out_attrs.get_attrs()
        in_attrs = self.widget_match_in_attrs.get_attrs()

        if len(out_attrs) != len(in_attrs):
            raise ValueError("out_attrs and in_attrs must have same length")

        func_type = self.widget_func_select.func()

        for o, i in zip(out_attrs, in_attrs):
            # Extract node names
            src_node = o.split('.')[0]
            dst_node = i.split('.')[0]

            if func_type == WidgetFuncSelect.Connect:
                cmds.connectAttr(o, i, force=True)
            elif func_type == WidgetFuncSelect.MatrixConnect:
                # source.worldMatrix[0] -> target.offsetParentMatrix
                cmds.connectAttr(
                    "{}.worldMatrix[0]".format(src_node),
                    "{}.offsetParentMatrix".format(dst_node),
                    force=True
                )
            elif func_type == WidgetFuncSelect.Disconnect:
                try:
                    cmds.disconnectAttr(o, i)
                except:
                    # try matrix disconnect
                    try:
                        cmds.disconnectAttr(
                            "{}.worldMatrix[0]".format(src_node),
                            "{}.offsetParentMatrix".format(dst_node)
                        )
                        cmds.setAttr("{}.offsetParentMatrix".format(dst_node),
                                     [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], type="matrix")
                    except:
                        cmds.warning("Disconnection failed between {} and {}".format(o, i))


def new():
    return WidgetConnections()