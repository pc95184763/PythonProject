
list1 = [100,200,300,400,500]
print( id(list1) )
list1[2:4] = ["a","b","c","d"]

print( list1 )
print( id(list1) )

list2 = list1[:]
print( id(list2) )