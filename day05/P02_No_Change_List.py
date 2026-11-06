import copy


def change_list(my_list):
    print(f"在函数体内部修改前的地址{id(my_list)}以及内容{my_list}")
    my_list[2] = 666
    print(f"在函数体内部修改后的地址{id(my_list)}以及内容{my_list}")


ml = [1,2,3]
print(f"在函数体外部修改前的地址{id(ml)}以及内容{ml}")

list2 = copy.copy(ml)
change_list(list2)
print(f"在函数体外部修改后的地址{id(ml)}以及内容{ml}")






