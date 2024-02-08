import random
import time
import sys
import os
from log import sessions
from nap import *
from taixiu import start_xocxoc1
from rut import rut_tien
from xoso import event_xosos
from otp import creator_otp
from kichhoat import kichhoat_otp

os.system('cls' if os.name == 'nt' else 'clear')

sessions()

os.system('cls' if os.name == 'nt' else 'clear')

with open('assets/xu.txt', 'r') as xu:
    xu = int(xu.read())
    xu1 = "{:,}".format(xu)

with open('data/data_info/nickname.txt', 'r') as nickname:
    nickname = nickname.read()

print(""""
==========================
Tên Nhân Vật : {}
Số Dư : {}$
==========================
""".format(nickname, xu1))

print("""
.------..------..------..------..------.
|8.--. ||8.--. ||8.--. ||G.--. ||B.--. |
| :/\: || :/\: || :/\: || :/\: || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() |
| '--'8|| '--'8|| '--'8|| '--'G|| '--'B|
`------'`------'`------'`------'`------'
=====Mini Game=====
1, Tài Xỉu Săn Hũ
2, Event Xổ Số (Thắng x60)
3, Nạp Xu
4, Rút Tiền
5, Lấy Code OTP
6, Bảo Mật Tài Khoản
===================
""")

user_input = input("Chọn Chế Độ : ")

if user_input == "1":
    start_xocxoc1()
if user_input == "2":
    event_xosos()
if user_input == "3":
    naps()
if user_input == "4":
    rut_tien()
if user_input == "5":
    creator_otp()
if user_input == "6":
    kichhoat_otp()
else:
    print("VUI LÒNG CHỌN...")
    exit()