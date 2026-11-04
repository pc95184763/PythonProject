
# 浅拷贝
import copy

def change_list(my_list):

    print(f"函数内list地址:{id(my_list)}以及内容：{my_list}")
    my_list[3].append("hello")
    print(f"函数内list地址:{id(my_list)}以及内容：{my_list}")


ml = [1, 2, 3, [1,2,3,4] ]
print(f"函数wai list地址:{id(ml)}以及内容：{ml}")

list2 = copy.deepcopy(ml)

change_list( list2 )
print(f"函数wai list地址:{id(ml)}以及内容：{ml}")












