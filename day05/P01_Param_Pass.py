# def func_info( name= "zhangSheng", age=10) :
#     print(f"姓名是{name}, 年龄{age}")
#
# func_info( age = 99)
#
# def func1(gender, name="auguigu", age = 111 ):
#     print(f"gender:{gender}, name:{name}, age:{age}")
#
# func1(9999)

# def printInfo(num, **hhh):
#     print(num, hhh)
# printInfo(1, a= 2,b=3,c=4 , num2=100  )


# 解包传参

def func(a,b,c) :
    print(a,b,c)

# tup1 = (10,20,30)
# func( *tup1 )
#
# dict1 = {"a":1, "b":2, "c":3}
# func(**dict1)


def f(a, b, /, c, d, *, e, f):
    print(a,b,c,d,e,f)




