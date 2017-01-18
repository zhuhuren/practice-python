#! mypython.py
import pkg
##import reloadall
__package__ = 'pkg'
test = 'test'
from . import modules
print(modules.x)

from .modules import func
func()

##import pkg.modules
##print(pkg.modules.module_x)

##print(__name__)
##from .pkg1 import spam


##print(spam.spam_x)


