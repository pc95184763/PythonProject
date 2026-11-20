"""
    演示了全局变量以及局部变量
"""


"""
sum = 0

def add(num1, num2): # 形参相当于定义在局部变量
    print(sum )

add(1,2)
print(sum)
"""

sum = 0

def add(num1, num2):
    sum = num1 + num2
    print("函数内局部变量的zhi", sum, id(sum) )
    return sum

add(10,20)






"""
    该案例演示了全局变量以及局部变量
"""


"""
sum = 0
def add(num1, num2):  # 形参相当于定义在函数内部的局部变量, 只能在函数内部被访问
    print(sum)

add(1,2)
"""

#  全局变量
"""
sum = 0

def add(num1, num2):
    sum = num1 + num2   # 这是一个局部变量
    print("函数内局部变量的值", sum, id(sum) )
    return sum

add(10,22)
print("函数外全局变量:", sum, id(sum) )
"""

# global 关键字
# var1 = 100
# def func():
#     # print(var1)
#     global var1
#     var1 += 10
#     return var1
#
# print( func() )

"""
var1 = [1,2,3]
def func():
    # var1.append(400)
    var1 = [3,4,5]
    return var1

print( func() )
print(var1 )
"""


def outer():
    var1 = 1
    print(var1)
    def inner():
        nonlocal var1
        var1 = 200
    inner()
    print(var1)

outer()


