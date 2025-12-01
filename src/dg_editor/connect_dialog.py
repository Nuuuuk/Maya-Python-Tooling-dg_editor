"""
Maya node filtering using Regex
return all maya nodes in scene that match the regex
"""

# for py2
from __future__ import unicode_literals, print_function
import re
import maya.cmds as cmds


def get_matched_nodes(pattern):
    """
    Yields nodes that strictly match the pattern.
    """
    if not pattern:
        return
    try:
        # Pre-compile regex
        regex_obj = re.compile(pattern)
    except re.error:
        print("Invalid Regex Pattern")
        return

    # Get all nodes, then filter
    all_nodes = cmds.ls('*')
    for node in all_nodes:
        attrs = cmds.listAttr(node) or []
        for attr in attrs:
            attr = "{}.{}".format(node, attr)
            m = regex_obj.match(attr)
            if not m is None:
                if m.group(0) == attr:
                    yield attr