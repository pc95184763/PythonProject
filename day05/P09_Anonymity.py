"""
    演示了匿名函数
"""
# num1, num2 是参与运算的两个数

"""
def op_1(a, b):
    return a + b
def op_2(a,b):
    return a - b

def op_3(a, b):
    return a * b

def op_4(a,b):
    return a / b

def calculate(num1, num2, op):
    return op(num1, num2)

print(calculate(1,2, op_3) )

print(calculate(3, 5, lambda a,b: a + b ) )

print(calculate(3, 5, lambda a,b: a - b ) )
"""


student_list = [ {"name": "zhang", "age": 36}, {"name":"lisi", "age": 24} , {"name":"wang5", "age": 27} ]

print( sorted(student_list, key=lambda x: x["age"])  )


# lambda map
def xx(item) :
    return item *2

print( list( map(lambda x:x*2, [1,2,3]) ) )

# filter

filter_result = filter( lambda x : x >=0 , [-1,3,4,-5,8,12])
print( list(filter_result)  )

# 归约
from functools import reduce

reduce_res = reduce( lambda x, y: x + y, [1,2,3,4,5] )
print(reduce_res )


# 实现自己的map

def my_map(m_list, op):
    for i, item in enumerate(m_list):








