#!python
"""
reloadall.py: transitively reload nested modules (2.X + 3.X).
Call reload_all with one or more imported module module objects.
"""
import types
from imp import reload                                   # from required in 3.X
def status(module):
    print('reloading ' + module.__name__)
def tryreload(module):
    try:
        reload(module)                                   # 3.3 (only?) fails on some
    except:
        print('FAILED: %s' % module)
def transitive_reload(module, mods_list):
##    if not module in mods_list:                            # Trap cycles, duplicates
##        status(module)                                   # Reload this module
##        tryreload(module)                                # And visit children
        for attrobj in module.__dict__.values():         # For all attrs
            if type(attrobj) == types.ModuleType:        # Recur if module
                mods_list.append(attrobj)
                transitive_reload(attrobj, mods_list)
def reload_all(*args):
    mods_list = []                                         # Main entry point
    for arg in args:                                     # For all passed in
        if type(arg) == types.ModuleType:
            mods_list.append(arg)
            transitive_reload(arg, mods_list)
    mods_list.reverse()
    for mod in mods_list:
        status(mod)
        tryreload(mod)
##    print(mods_list)

def tester(reloader, modname):                           # Self-test code
    import importlib, sys                                # Import on tests only
    if len(sys.argv) > 1: modname = sys.argv[1]          # command line (or passed)
    module  = importlib.import_module(modname)           # Import by name string
    reloader(module)                                     # Test passed-in reloader
if __name__ == '__main__':
    tester(reload_all, 'reloadall')                      # Test: reload myself?
