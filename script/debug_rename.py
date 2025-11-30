import importlib as imp
import init
import rename as rename
import maya.mel as mel

# reload
imp.reload(init)

mel.eval("""
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// Result: pSphere1 polySphere1
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
duplicate -rr;
// Result: group6 //
""")

rename.add_name_prefix("_")
rename.search_n_replace("gr", "GR")
rename.regex_search_n_replace("o.p", "OUP")