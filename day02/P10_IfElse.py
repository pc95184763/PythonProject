from random import randint
price = 50


balance = randint(0, 100)
print(f"余额为: {balance}")
if ( balance < price ):
    print(f"余额不足")
else :
    print("消费成功")

print("欢迎下次光临")


