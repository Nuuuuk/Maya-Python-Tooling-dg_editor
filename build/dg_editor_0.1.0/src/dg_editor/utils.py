import maya.cmds as cmds
import functools

from . import settings


def undo_block(fn):
    @functools.wraps(fn)
    def _(*args, **kwargs):
        enable_undo = settings.get_undo_check()

        if enable_undo:
            cmds.undoInfo(ock=True)

        try:
            return fn(*args, **kwargs)
        finally:
            cmds.undoInfo(cck=True)

    return _