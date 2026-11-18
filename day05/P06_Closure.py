"""
    该案例演示了闭包
"""
# 可以让当前函数中定义的变量能够在其他函数中被访问

#  嵌套调用实现
# def func1():
#     num1 = 10
#     func2(num1)
#
# def func2(num1):
#     print(num1)
#
# func1()

# 闭包：
# 外部函数内定义一个内部函数
# 内部函数用到外部函数中的变量
# 外部函数将背部函数作为返回值

# 闭包实现
# def outer():
#     num1 = 10
#
#     def inner():
#         print(num1)
#
#     return inner
#
# inn = outer()
# inn()

a = 10
def outer():
    num1 = 10
    b = 20  # 嵌套作用域
    def inner():
        c = 30  # 局部作用域
        print("先从局部作用域找:", c)
        print("先从嵌套作用域找:", b)
        print("先从全局作用域找:", a)
        print("最后从内建作用域中找", len([1, 2, 3]))
    return inner

inn = outer()
inn()








