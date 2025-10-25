import importlib as imp
import config

# reread config so that the change to config (DEBUG) can be effective immediately
imp.reload(config)

if config.DEBUG:
    # reload everything
    pass
