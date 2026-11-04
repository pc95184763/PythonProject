

tuple1 = (100,200,300,400,500)
tuple2 = ("a","b","c")
tup = tuple1 +tuple2

print( tuple1, id(tuple1) )
print( tuple2, id(tuple2) )
print( tup, id(tup) )

tup2 = tuple1 + tuple2

print( tup2, id(tup2)  )



