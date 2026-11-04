

def printStar(row, col) :

    while row > 0 :
        print("*" * col)
        row -= 1

printStar(3,3 )


def changeInt(a):
    print("函数体中未改变前a的内存地址", id(a) )
    a = 10
    print("函数体中改变后a的内存地址: ", id(a))

b = 2;
changeInt(b)
