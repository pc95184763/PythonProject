

def changeList(myList):
    print("改变前list的值", myList, id(myList))
    myList = myList * 2
    print("函数中改变后list的值", myList, id(myList) )

mlist = [1,2,3]

changeList(mlist)

print(mlist, id(mlist) )


