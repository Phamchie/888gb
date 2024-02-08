import random
import time
import os
from event_xoso import events

def event_xosos():
    try:
        def profile():
            # nickname
            with open('data/data_info/nickname.txt', 'r') as nickname:
                nickname = nickname.read()
            # coins
            with open('assets/xu.txt', 'r') as coins:
                coins = int(coins.read())
                coins = "{:,}".format(coins)

            print("================")
            print("Tên Nhân Vật : {}".format(nickname))
            print("Số Dư : {}".format(coins))
            print("================")
        os.system('cls' if os.name == 'nt' else 'clear')
        profile()
        print("""
.------..------..------..------..------.
|8.--. ||8.--. ||8.--. ||G.--. ||B.--. |
| :/\: || :/\: || :/\: || :/\: || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() |
| '--'8|| '--'8|| '--'8|| '--'G|| '--'B|
`------'`------'`------'`------'`------'
""")
        print("=====================")
        print("1, Chơi Event Xổ Số")
        print("2, Lịch Sử Cược")
        print("=====================")
        user_input = input('Vui Lòng Chọn : ')
        if user_input == "1":
            events()
        if user_input == "2":
            with open('assets/lichsu_xoso.txt', 'r') as lichsu:
                lichsu = lichsu.read()
                print(lichsu)
    except:
        print("Error")
        exit()
   