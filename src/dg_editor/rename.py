# for py2
from __future__ import unicode_literals, print_function

import re
import maya.cmds as cmds

def _select_uids():
    sel = cmds.ls(sl=True, long=True)

    if not sel:
        return []

    nodes = [
        n for s in sel
        for all_nodes in ([s], cmds.listRelatives(s, ad=True, pa=True) or [])
        for n in all_nodes
    ]
    uids = cmds.ls(nodes, uid=True)
    return list(set(uids)) # remove repeated, in case selected child and parent simultaneously

def add_name_prefix(prefix):
    for uid in _select_uids():
        node = cmds.ls(uid)[0]
        cmds.rename(node, prefix + node.split('|')[-1])

def add_name_suffix(suffix):
    for uid in _select_uids():
        node = cmds.ls(uid)[0]
        cmds.rename(node, node.split('|')[-1] + suffix)

def search_n_replace(search, replace):
    for uid in _select_uids():
        node = cmds.ls(uid)[0]
        node_name = node.split('|')[-1]
        cmds.rename(node, node_name.replace(search, replace))

def regex_search_n_replace(search, replace):
    regex_obj = re.compile(search)
    for uid in _select_uids():
        node = cmds.ls(uid)[0]
        node_name = node.split('|')[-1]
        cmds.rename(node, regex_obj.sub(replace, node_name))

