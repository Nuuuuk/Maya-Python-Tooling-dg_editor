# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

# import modules needed
import config

import exp_parser_node_create
import dialog_exp_gen
import dialog_del_match

import widget_nodes, widget_connections
import my_window


# reload config at first
imp.reload(config)

modules = [
    exp_parser_node_create,

    dialog_exp_gen,
    dialog_del_match,

    widget_nodes,
    widget_connections,
    my_window,
]

if config.DEBUG:
    # reload everything
    for m in modules:
        imp.reload(m)

else:
    pass
