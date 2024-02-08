import random
import os
import time
from nap import naps

def start_xocxoc1():
    while True:
        xhu = random.randint(10, 88)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
.------..------..------..------..------.
|8.--. ||8.--. ||8.--. ||G.--. ||B.--. |
| :/\: || :/\: || :/\: || :/\: || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() |
| '--'8|| '--'8|| '--'8|| '--'G|| '--'B|
`------'`------'`------'`------'`------'
""")
        with open('assets/xu.txt', 'r') as so_du:
            so_du = int(so_du.read())
            so_du1 = "{:,}".format(so_du)

        with open('data/data_info/nickname.txt', 'r' ) as nickname:
            nickname = nickname.read()

        print("Tên Nhân Vật : {}".format(nickname))
        print("Số Dư : {}đ".format(so_du1))
        print("""
===TÀI XỈU===
   1, TÀI
   2, XỈU
   3, Thoát 
   4, Lịch Sử Cược
=============
    """)

        user_input = input("Vui Lòng Chọn : ")
        if user_input == "3":
            exit()
        
        if user_input == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            with open('assets/lichsu_taixiu.txt', 'r') as lichsu:
                lichsu = lichsu.read()
                print(lichsu)

        tien_cuoc = int(input("Nhập Số Tiền Cược : "))

        if tien_cuoc > so_du:
            print("Bạn Không Đủ Tiền Để Cược, Vui lòng Nạp Thêm Tiền")
            naps()
            print("")
            exit()

        tien_cuoc1 = "{:,}".format(tien_cuoc)
        if user_input == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            so_du1 = int(so_du - tien_cuoc)
            so_du1 = "{:,}".format(so_du1)
            print("""
Đặt Cược Thành Công
Đặt : TÀI
Số Tiền Cược : {}đ
Số Dư Còn Lại : {}đ
    """.format(tien_cuoc1, so_du1))

            def start_xoc():
                print("vui Lòng Chờ trong 10 giây")
                time.sleep(10)
                print("Bắt Đầu Xóc...")
                time.sleep(1)
                xucxac1 = random.randint(1, 6)
                xucxac2 = random.randint(1, 6)
                xucxac3 = random.randint(1, 6)
                ket_qua = int(xucxac1 + xucxac2 + xucxac3)
                tai = [11,12,13,14,15,16,17]
                xiu = [3,4,5,6,7,8,9,10]
                if ket_qua == 18:
                    print("==========================")
                    print("Kết Quả")
                    print("TÀI : {}".format(ket_qua))
                    print("Kq Xí Ngầu : {} - {} - {}".format(xucxac1, xucxac2, xucxac3))
                    cong_tien = int(tien_cuoc * 2 * xhu - (tien_cuoc * 2 / 100))
                    ct = "{:,}".format(cong_tien)
                    print("Nổ Hũ")
                    print("Tiền Thắng : +{}đ".format(ct))
                    so_du0 = str(so_du + cong_tien - tien_cuoc)
                    so_du2 = int(so_du + cong_tien - tien_cuoc)
                    so_du1 = "{:,}".format(so_du2)
                    print("Số Dư : {}đ".format(so_du1))
                    print("==========================")
                    with open('assets/xu.txt', 'w') as so_du3:
                        so_du3 = so_du3.write(so_du0)

                    with open('assets/lichsu_taixiu.txt', 'r') as lichsu:
                        history = lichsu.read()
                    
                    with open('assets/lichsu_taixiu.txt', 'w') as lich_su:
                        htr = f"[-] Dat TAI {tien_cuoc1}$, Ket Qua {xucxac1}-{xucxac2}-{xucxac3} TAI, Hoan Tra 0, Nhan +{ct}$"
                        ls = f"""{history}
{htr}"""
                        lich_su.write(ls)

                if ket_qua in tai:
                    print("==========================")
                    print("Kết Quả")
                    print("TÀI : {}".format(ket_qua))
                    print("Kq Xí Ngầu : {} - {} - {}".format(xucxac1, xucxac2, xucxac3))
                    cong_tien = int(tien_cuoc + tien_cuoc - (tien_cuoc * 2 / 100))
                    ct = "{:,}".format(cong_tien)
                    print("Tiền Thắng : +{}đ".format(ct))
                    so_du0 = str(so_du + cong_tien - tien_cuoc)
                    so_du2 = int(so_du + cong_tien - tien_cuoc)
                    so_du1 = "{:,}".format(so_du2)
                    print("Số Dư : {}đ".format(so_du1))
                    print("==========================")
                    with open('assets/xu.txt', 'w') as so_du3:
                        so_du3 = so_du3.write(so_du0)

                    with open('assets/lichsu_taixiu.txt', 'r') as lichsu:
                        history = lichsu.read()
                    
                    with open('assets/lichsu_taixiu.txt', 'w') as lich_su:
                        htr = f"[-] Dat TAI {tien_cuoc1}$, Ket Qua {xucxac1}-{xucxac2}-{xucxac3} TAI, Hoan Tra 0, Nhan +{ct}$"
                        ls = f"""{history}
{htr}"""
                        lich_su.write(ls)

                if ket_qua in xiu:
                    print("==========================")
                    print("Kết Quả")
                    print("XỈU : {}".format(ket_qua))
                    print("Kq Xí Ngầu : {} - {} - {}".format(xucxac1, xucxac2, xucxac3))
                    print("Tiền Thắng : 0đ")
                    so_du0 = str(so_du - tien_cuoc)
                    so_du2 = int(so_du - tien_cuoc)
                    so_du1 = "{:,}".format(so_du2)
                    print("Số Dư : {}đ".format(so_du1))
                    print("==========================")
                    with open('assets/xu.txt', 'w') as so_du3:
                        so_du3 = so_du3.write(so_du0)
                    
                    with open('assets/lichsu_taixiu.txt', 'r') as lichsu:
                        history = lichsu.read()
                    
                    with open('assets/lichsu_taixiu.txt', 'w') as lich_su:
                        htr = f"[-] Dat TAI {tien_cuoc1}$, Ket Qua {xucxac1}-{xucxac2}-{xucxac3} XIU, Hoan Tra 0, Nhan 0$"
                        ls = f"""{history}
{htr}"""
                        lich_su.write(ls)
            start_xoc()

        if user_input == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            so_du1 = int(so_du - tien_cuoc)
            so_du1 = "{:,}".format(so_du1)
            print("""
Đặt Cược Thành Công
Đặt : XỈU
Số Tiền Cược : {}đ
Số Dư Còn Lại : {}đ
    """.format(tien_cuoc1, so_du1))

            def start_xoc():
                print("vui Lòng Chờ trong 10 giây")
                time.sleep(10)
                print("Bắt Đầu Xóc...")
                time.sleep(1)
                xucxac1 = random.randint(1, 6)
                xucxac2 = random.randint(1, 6)
                xucxac3 = random.randint(1, 6)
                ket_qua = int(xucxac1 + xucxac2 + xucxac3)
                tai = [11,12,13,14,15,16,17,18]
                xiu = [4,5,6,7,8,9,10]
                if ket_qua == 3:
                    print("==========================")
                    print("Kết Quả")
                    print("XỈU : {}".format(ket_qua))
                    print("Kq Xí Ngầu : {} - {} - {}".format(xucxac1, xucxac2, xucxac3))
                    cong_tien = int(tien_cuoc * 2 * xhu - (tien_cuoc * 2 / 100))
                    ct = "{:,}".format(cong_tien)
                    print("Nổ Hũ")
                    print("Tiền Thắng : +{}đ".format(ct))
                    so_du0 = str(so_du + cong_tien - tien_cuoc)
                    so_du2 = int(so_du + cong_tien - tien_cuoc)
                    so_du1 = "{:,}".format(so_du2)
                    print("Số Dư : {}đ".format(so_du1))
                    print("==========================")
                    with open('assets/xu.txt', 'w') as so_du3:
                        so_du3 = so_du3.write(so_du0)

                    with open('assets/lichsu_taixiu.txt', 'r') as lichsu:
                        history = lichsu.read()
                    
                    with open('assets/lichsu_taixiu.txt', 'w') as lich_su:
                        htr = f"[-] Dat XIU {tien_cuoc1}$, Ket Qua {xucxac1}-{xucxac2}-{xucxac3} XIU, Hoan Tra 0, Nhan +{ct}$"
                        ls = f"""{history}
{htr}"""
                        lich_su.write(ls)

                if ket_qua in xiu:
                    print("==========================")
                    print("Kết Quả")
                    print("XỈU : {}".format(ket_qua))
                    print("Kq Xí Ngầu : {} - {} - {}".format(xucxac1, xucxac2, xucxac3))
                    cong_tien = int(tien_cuoc + tien_cuoc - (tien_cuoc * 2 / 100))
                    ct = "{:,}".format(cong_tien)
                    print("Tiền Thắng : +{}đ".format(ct))
                    so_du0 = str(so_du + cong_tien - tien_cuoc)
                    so_du2 = int(so_du + cong_tien - tien_cuoc)
                    so_du1 = "{:,}".format(so_du2)
                    print("Số Dư : {}đ".format(so_du1))
                    print("==========================")
                    with open('assets/xu.txt', 'w') as so_du3:
                        so_du3 = so_du3.write(so_du0)
                    
                    with open('assets/lichsu_taixiu.txt', 'r') as lichsu:
                        history = lichsu.read()
                    
                    with open('assets/lichsu_taixiu.txt', 'w') as lich_su:
                        htr = f"[-] Dat XIU {tien_cuoc1}$, Ket Qua {xucxac1}-{xucxac2}-{xucxac3} XIU, Hoan Tra 0, Nhan +{ct}$"
                        ls = f"""{history}
{htr}"""
                        lich_su.write(ls)

                if ket_qua in tai:
                    print("==========================")
                    print("Kết Quả")
                    print("TÀI : {}".format(ket_qua))
                    print("Kq Xí Ngầu : {} - {} - {}".format(xucxac1, xucxac2, xucxac3))
                    print("Tiền Thắng : 0đ")
                    so_du0 = str(so_du - tien_cuoc)
                    so_du2 = int(so_du - tien_cuoc)
                    so_du1 = "{:,}".format(so_du2)
                    print("Số Dư : {}đ".format(so_du1))
                    print("==========================")
                    with open('assets/xu.txt', 'w') as so_du3:
                        so_du3 = so_du3.write(so_du0)
                    
                    with open('assets/lichsu_taixiu.txt', 'r') as lichsu:
                        history = lichsu.read()
                    
                    with open('assets/lichsu_taixiu.txt', 'w') as lich_su:
                        htr = f"[-] Dat XIU {tien_cuoc1}$, Ket Qua {xucxac1}-{xucxac2}-{xucxac3} TAI, Hoan Tra 0, Nhan 0$"
                        ls = f"""{history}
{htr}"""
                        lich_su.write(ls)
            start_xoc()

        print("Bắt Đầu Phiên Mới")
        time.sleep(6)  