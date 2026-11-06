
# rabbit = 2
# week = 1
# while week < 10 :
#     rabbit = rabbit + rabbit * 2
#     week += 1
#     print(f"第{week}周有{rabbit}只兔子")
# else:
#     print(f"第{week}周有{rabbit}只兔子")



# import time
# num = 1;
#
# while num <= 100:
#     print("\r" + num * "=", end = "")
#     num += 1
#     time.sleep(0.5)

rabbit = 2
week = 1

while week < 10:
    rabbit = rabbit + rabbit * 2
    week += 1
    if week == 11:
        break
else :
    print(f"第{week}周有{rabbit}只兔子")
print("xxxxxa")



