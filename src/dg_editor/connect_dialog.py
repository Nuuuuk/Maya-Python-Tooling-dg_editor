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
    Yields nodes or node.attr that match the pattern.
    """
    if not pattern:
        return
    try:
        # Pre-compile regex
        regex_obj = re.compile(pattern)
    except re.error:
        print("Invalid Regex Pattern")
        return

    # Check if pattern is for node.attr or just nodes
    match_attrs = '.' in pattern

    # Get all nodes, then filter
    all_nodes = cmds.ls('*')
    for node in all_nodes:
        if match_attrs:
            # match node.attr
            attrs = cmds.listAttr(node) or []
            for attr in attrs:
                full_attr = "{}.{}".format(node, attr)
                m = regex_obj.match(full_attr)
                if not m is None:
                    if m.group(0) == full_attr:
                        yield full_attr
        else:
            # match node names only
            m = regex_obj.match(node)
            if m is not None and m.group(0) == node:
                yield node