
num1 = 17
#  00010001
#  11101110
#  -1101101
#  -0010010

num2 = 13
# 01101

num3 = -20
print( f"{num1} & {num2} : {num1 & num2:08b}")

print( f"{num1} | {num2} : {num1 | num2:08b}")


print(f"{num1 >> 3 }")

# num = 10
# list1 = [1,2,3,10]
# print( num not in list1)

bool1 = True
bool2 = False
num1 = 0
print( bool2 == num1 )
print( bool2  is not  num1)


import sys
for i in sys.path:
    print(i)



