
dict3 = {"name": "Alice", "age": 18, "gender": "male" }

dict4 = dict(name="Bob",age=20,gender="female")
print(dict4)

dict5 = dict( [ ("name", "Tom"),("age", 22),("gender", "male")] )
print(dict5)

squares = {x : x ** 2 for x in range(4) }
print(squares)

print( dict5.get("address") )

squares["address"] = "123 Main St."
print( squares )

print( 3 in squares)

dict1 = {"name": "Alice", "age": 81, "gender": "male"}
print(len(dict1) )

# 遍历字典
keys = dict1.keys()
for k in keys:
    print(k)
print("----"* 20)

vals = dict1.values()
for v in vals:
    print(v)
print("----" * 20)
for k in keys:
    print(k + "---" + str(dict1[k] ) )

kv = dict1.items()
for i in kv:
    print(i)

print("----" * 20)

for k, v in dict1.items():
    print(k, v)


# 遍历字典
dict1 = {"Name": "Tom", "Age": 17}
print(dict1)
del dict1["Name"]
print(dict1)
