

from random import randint

price = 50
balance = randint(0, 100)


if ( balance < price ):
    print(" 余额不足")

elif ( balance > price ):
    print(f"扣款成功, 余额: { (balance := balance - price)}")







