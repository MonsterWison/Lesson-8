# when main is loading util package __init__.py will run
# case 3:
print('__init__ is trigger')
COLOR = 'red'

# Re-export from test1.py
from .test1 import a, b, x

#case 4:
# from .test1 import a, b, x