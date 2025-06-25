# when main is loading util package __init__.py will run
# case 3:
print('__init__ is trigger')
COLOR = 'red'

#case 4:
# from .test1 import a, b, x

#case 4:
from .test1 import a, b, x
__all__ = ['a', 'COLOR'] #限制import的variable