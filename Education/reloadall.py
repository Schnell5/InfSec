'''
Reload all modules recursively

Usage:

import reloadall

reload_all(<module_name>)

'''

import types
from importlib import reload


def status(module):
    print('reloading ' + module.__name__)


def transitive_reload(module, visited):
    if module not in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attrobj in module.__dict__.values():
            if isinstance(attrobj, types.ModuleType):
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}
    for arg in args:
        if isinstance(arg, types.ModuleType):
            transitive_reload(arg, visited)


if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)

