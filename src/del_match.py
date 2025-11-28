"""
return all maya nodes in scene that match the regex 
"""

# for py2
from __future__ import unicode_literals, print_function
import re

import maya.cmds as cmds


def regex_match(exp):
    re_obj = re.compile(exp)
    for n in cmds.ls('*'):
        m = re_obj.match(n)
        if not m is None:
            if m.group(0) == n:
                yield n