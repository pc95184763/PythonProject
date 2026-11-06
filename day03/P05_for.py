# for i in [2,3,5,7,11,13,17,19]:
#     print(i)
#
# for i in "hello world":
#     print(i)


# for i in range(1, 10):
#     for j in range(1, i + 1) :
#         print(f"{i} x {j} = {i * j}", end="\t")
#     print("")


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

sum = 0
for i in range(10):
    sum += i ** i
    if sum > 10000000:
        break
    print(i, sum)


print(f"循环完成, sum ={sum} i = {i}")
