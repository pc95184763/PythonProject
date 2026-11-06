"""
    演示了变量
"""
# 将10 复制给a这个变量

# a = 10
# b = 20
# c = a + b
# print(c)


var1 = var2 = var3 = 10
# 不可变数据类型
print(id(var1), id(var2), id(var3))
var1 = 20
print(id(var1), id(var2), id(var3))
print("~~~~~~~~~~~~~~")

# 可变数据类型
a = b = c =[1,2,3]
print(id(a), id(b), id(c))
a.append(4)
print(id(a), id(b), id(c) )
print( b)

print("~~~~~~~~~~~~~~")
var4, var5 = 20, 30

print( var4, var5)






