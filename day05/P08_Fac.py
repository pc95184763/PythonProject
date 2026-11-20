"""
    该案例演示了递归求阶乘
"""
# 循环求
def fac(n ):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
print( fac(5) )


def fac1(n):
    if n == 1 :
        return 1
    return n *fac1(n - 1)

print( fac1(5) )