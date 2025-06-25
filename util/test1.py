def a():
    print("I am from test1.py function a")

def b():
    print("I am from test1.py function b")
def _c(_d):
    print("private function within test1")
    _d()
def _d():
    print("private function within test1")

x = 10
_y = 20