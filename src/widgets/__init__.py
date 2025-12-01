# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

# import modules needed
import config

from . import base

if config.DEBUG:
    imp.reload(base)

# expose class in init
from .base import BaseWidget