# for py2
from __future__ import unicode_literals, print_function

import sys
import importlib as imp

# import modules needed
import config
import my_window

# reload config at first
imp.reload(config)

if config.DEBUG:
    # reload everything
    imp.reload(my_window)
else:
    pass
