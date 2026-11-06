

def changeInt(a):
    print(id(a))
    a = 10
    print("函数内改变后: ", id(a))

b = 2
changeInt(b)
print(b)
print("函数外b: ", id(b))