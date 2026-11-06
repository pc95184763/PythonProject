"""
    案例演示了元组
    1. 创建：逗号
    2. 元组 推导式
    3. 元组不可变.

"""

# 元组中只有一个元素时, 需要再元素后面加逗号, 否则括号会被当运算符
# tup0= (100,200,300, '500')
# tup1 = (100)
#
# print( tup0 )
# print( type(tup1) )


# 列表推导式
# list1 = [i * 3 for i in range(15) ]
# print(list1)

# 元组推导式, 直接返回生成器
# gen1 = (i * 3 for i in range(10) )
# print(gen1)
# tup111 = tuple(gen1)
# print(tup111)
# print( tup111[0:-1])

# tuple1 = (100,200,300,400,500)
# print(tuple1)
# print(tuple1[1:] )

# tup1 = (1, 2, 3 )
# tup2 = ("a","b", "c","d","e","f")
#
# print( sum(tup1) )
# print( max(tup1) )
# print( min(tup1) )

# 元组遍历
# tup1 = (3,10,17,13,9,'a', "AWS")
# for item in tup1:
#     print(item)

# for i in range( len(tup1) ) :
#     print(tup1[i] )
#
# for i, val in enumerate(tup1) :
#     print(i, val)


# tup1 = (257,2,3,[3,2,257])
# print(tup1)
# tup1[3].append(117)
# print(tup1)


# print( id(tup1[0] ) )
# print( id(tup1[3][2] ) )


# 块1
tup1 = (257,2,3,[3,2,1])

# 块2，模拟分开编译，动态构造list，257不再是源码字面量
lst = [3,2]
lst.append(257)
tup2 = (257, 2,3, lst)

print(id(tup2[0]))
print(id(tup2[3][2]))
# id 不相等！257不是同一块源码里写死的字面量





