#! modules.py
from .pkg1 import spam
x = 'module_x' + ' : ' + spam.x

##import pkg.pkg1.spam
##module_x = 'module_x_1' + ' : ' + pkg.pkg1.spam.spam_x

##def adder(a, b):
##    return a + b
##

def func():
    print('I\'m in modules.py. yes')
##
##def func1():
##    pass

from . import mypython
print(mypython.test)

##name1= 'austin'
##name2 = 'anna'
##name3 = 'winsor'

##__all__ = ['adder', 'func']
