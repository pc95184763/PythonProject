
match month := 3 :
    case 1|3|5|7|8|10|12:
        print(f"{month}月有31天")
    case 4|6|9|11:
        print(f"{month}月有30天")
    case _:
        if month % 4 == 0 or month % 400 == 0 :
            print(f"{month} 有29天")




