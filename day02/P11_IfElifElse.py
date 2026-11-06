from random import randint

print("age= ", age := randint(0, 80 ) )

if age < 2 :
    print("婴儿")
elif age < 4 :
    print("幼儿")
elif age < 13 :
    print("儿童")
elif age < 20 :
    print("青少年")
elif age < 65 :
    print("这个人是成年人")
else :
    print("老年人!")



