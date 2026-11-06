# 创建

# set1 = set( [1,2,3,5,3,1])
# set2 = set()
# print( type(set2) )

#  集合推导式
# set3 = { i * 5 for i in range(10) }
#
# print( set3)

#  添加
# set4 = {1,2,3}
# print( set4, id(set4) )
# set4.remove(2)
# print( set4, id(set4) )


#  成员运算

# print(5 in set1 )
# print( len(set1) )
# print( max(set1) )
# print( min(set1) )
# print( sum(set1) )

#  没有通过下标的遍历方法
# for item in set1:
#     print(item)

# 集合Set常用函数
# set1 = {1,2,3}
# set1.update([1,2,4,8,8, 10])

# print( set1 )
#
# set3 = set1.union( ('a','b', 131))
# print(set3 )
# set3.remove(30)
# print(set3)
# set1.discard(30)
# print(set3)
# print( set3.pop() )
# print(set3)
# set3.clear()
# print(set3)


set5 = {4,5,6,3}
set4 = {3,4,5}

set2 = set4.symmetric_difference(set5)
set4.symmetric_difference_update(set5)

print(set2)
print(  set4 )
