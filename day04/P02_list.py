list1 = [100,200,300,400,500]
print( list1[0] )
print( list1[2:] )
print( list1[:2])
print( list1[2:-1] )

#
list1.append( 600 )
list1.insert(2, 1000 )
print( list1 )
print( id(list1) )
print("======--------------------------------======")

for i in range( len(list1) ):
    print( list1[i] )

for i, val in enumerate( list1):
    print( i, list1[i] )

del list1[3]

print( list1)

list2 = [ [1,2,3],[4,5,6],[7,8,9] ]
for inner_list in list2:
    print( inner_list )

print("*********************************")

squares = [ x ** 2 for x in range(10) ]
print( squares)


squares = [x ** 2 for x in range(10) if x % 3 == 0 ]
print( squares)

list2 = [1,2,3,4,5]
squares = [ x ** 2 for x in list2 ]
print( squares )

list3 = [1,2,3,4,5,6]
list4 = ["a","b","c","d","e","f","g"]
tuple_list = [ (i, j) for i in list3 for j in list4 ]
print( tuple_list)
print("*********************************")

zipped = zip( list3, list4 )
print( list(zipped)  )



