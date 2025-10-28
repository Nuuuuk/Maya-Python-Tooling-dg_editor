# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

# import modules needed
import config

import create_node_exp
import dialog_exp_gen

import widget_nodes, widget_connections
import my_window


# reload config at first
imp.reload(config)

if config.DEBUG:
    # reload everything
    imp.reload(create_node_exp)
    imp.reload(dialog_exp_gen)

    imp.reload(widget_nodes)
    imp.reload(widget_connections)
    imp.reload(my_window)

else:
    pass
