# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

# import modules needed
import config
import widget_nodes, widget_connections
import my_window

import create_node_exp

# reload config at first
imp.reload(config)

if config.DEBUG:
    # reload everything
    imp.reload(widget_nodes)
    imp.reload(widget_connections)
    imp.reload(my_window)

    imp.reload(create_node_exp)
else:
    pass
