# P1

# list1 = [100, 200,300,400,500]
# list1.append(600)
# print(list1)
# list1.insert(2,700)
# print(list1)

# P2
# list2 = [100,200,301]
# list3 = ["a","b","c"]
# list4 = list2+list3
# print( id(list2), id(list3), id(list4) )
# list1 = [101,202,303]
# listX = list1 * 3
# print( id(list1), id(listX) )

# P3
# a = [1,2]
# print(id(a))
# a = a + [3,4]   # + 产生新列表，变量a指向新地址
# print(id(a))
#
# b = [1,2]
# print(id(b))
# b += [3,4]      # += 原地extend，id不变
# print(id(b))

# P4
# list1 = [100,200,300,400,500 ]
# print( sum(list1) )

# for i in list1:
#     print(i)

# for i in range( len(list1) ):
#     print( i, list1[i] )

# for i, val in enumerate(list1):
#     print(i, val)

# P5
# list1 = [ [1,2,3], [4,5,6],[7,8,9,10] ]
# for inner_list in list1:
#     print(inner_list)

# P6
# squares = [ x ** 2 for x in range(5) ]
# print(squares)
#
# squares1 = [ x** 3 for x in range(10) if x % 2 == 0 ]
# print(squares1)
#
# list1 = [1,2,3,4,5]
# squares2 = [x ** 2 + 9 for x in list1]
# print(squares2 )

# P7
# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]

# tuple_list = [(i,j) for i in list1 for j in list2 if i % 2== 0 and j <= "c"]
# print( tuple_list )

# P8
list1 = [1,2,3,4,5,6,7,8,9]
list2 = ["a","b","c","d","e" ]

zipped = zip(list1, list2)
for i in zipped:
    print(i)

