def a():
    print("I am from main.py function a")
def b():
    print("I am from main.py function b")
# a()
# b()

#case 1: simply import module
# import test
# test.a()
# test.b()
# print(test.x)
# print(test._y)

# case 1.1: import module with alias
# import test as t
# t.a()
# t.b()
# print(t.x)
# print(t._y)

# # case 2 : 可select
# from test import a, x, _y
# a()
# b()
# print(x,_y)

# case 2.1: effect is same as case 1
# from test import *
# a()
# b()
# print(x,_y)

#case 2.2: 
# from test import a as ta, x as tx, _y as t_y
# ta()
# b()
# print(tx,t_y)

# case 3: import module from sub-folder without __init__
# same as effect as case 2.1 ut private variable won't load
# from util.test1 import *
# a()
# b()
# print(x)

# case 3.1:
# from util.test1 import *
# a()
# b()
# from util import COLOR
# print(COLOR)
# print(x)

# case 4:
# from util import a, b, x, COLOR
# a()
# b()
# print(COLOR, x)

# case 4.1:
# from util import *
# a()
# b()
# print(COLOR)

#===================================
# input function
name = input('please input your name: ')
print(name)
age = input("please input your age: ")
age = float(age) * 365.25
print(age)

