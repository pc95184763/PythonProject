"""
    案例演示了输出
"""


#  使用 % 占位
int1 = 10
float1 = 3.14159
bool1 = True
print("int1 = %d, float1 = %f, bool1 = %s" % (int1, float1, bool1) )

print("int1 = {2}, float1 = {1}, bool1 = {0}".format (int1, float1,bool1) )


#  数字格式化
float2 = 31415.8136

str2 = "{:*^20,.3f}".format(float2)
print(str2)


print( "{0} 对应的位置是 {0}".format("hello") )

# f - 字符串
int1 = 10
float1 = 3.14159
print(f"int1 = {int1}, float1= {float1}")
print(f"{int1}, {float1}")

