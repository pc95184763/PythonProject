
num = 0b111

if num & 0b100 == 0b100 :
    print("大写状态")
else :
    if num & 0b010 == 0b010 :
        if num & 0b001 == 0b001:
            print("简体中文 - 中文模式")
    else :
        print("英语-美式键盘")


