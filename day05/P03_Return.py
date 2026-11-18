"""
    该案例演示了return关键字
"""

def func():
    for i in range(10):
        if i == 7:
            # continue 跳过当前正在进行的本次循环
            # break 结束整个循环
            # return 结束整个func, 返回
            continue
        print(i)
    print("循环结束了")

func()


def add(num1, num2):
    return num1 + num2



