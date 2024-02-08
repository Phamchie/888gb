import random
import time
import os
from nap import naps

def events():
    phien = 0
    while True:
        phien += 1
        giai_dac_biet = random.randint(1, 99)

        def usr():
            os.system('cls' if os.name == 'nt' else 'clear')
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
            profile()
            user_input1 = input("Chọn Cược Một Con Số Từ 1 đến 99 [1] : ")
            user_input2 = input("Chọn Cược Một Con Số Từ 1 đến 99 [2] : ")
            user_input3 = input("Chọn Cược Một Con Số Từ 1 đến 99 [3] : ")
            user_input4 = input("Chọn Cược Một Con Số Từ 1 đến 99 [4] : ")
            user_input5 = input("Chọn Cược Một Con Số Từ 1 đến 99 [5] : ")
            tien_cuoc = int(input("Nhập Số Tiền Cược Cả 5 Tay : "))
            tien_cuoc1 = "{:,}".format(tien_cuoc)
            # kiểm tra nếu người chơi nhập tiền cược quá số dư hiện tại
            with open('assets/xu.txt', 'r') as so_du_hien_tai:
                so_du = so_du_hien_tai.read()
                so_du_hien_tai = int(so_du)
            if tien_cuoc > so_du_hien_tai:
                print("Bạn Không Đủ Tiền Để Cược")
                naps()
                exit()
            def cuoc_thanhcong():
                print("==========================")
                print("Số Đặt Cược : {}, {}, {}, {}, {}".format(user_input1, user_input2, user_input3, user_input4, user_input5))
                print("Số Tiền Cược : {}$".format(tien_cuoc1))
                print("Phiên : #{}".format(phien))
                print("==========================")
            cuoc_thanhcong()
            print("Vui Lòng Chờ Kết Quả Trong 10 Giây Nữa")
            time.sleep(10)
            if user_input1 == giai_dac_biet:
                print("===================")
                print("Bạn Đã Trúng Giải")
                print("Phiên : #{}".format(phien))
                print("Số Chọn Cược : {}, {}, {}, {}, {}".format(user_input1, user_input2, user_input3, user_input4, user_input5))
                print("Số Trúng : {}".format(giai_dac_biet))
                print("Tiền Cược : {}$".format(tien_cuoc1))
                tien_thang = int(tien_cuoc * 2 * 60 - (tien_cuoc * 10 / 100))
                tienthang = "{:,}".format(tien_thang)
                so_du1 = str(so_du_hien_tai + tien_thang)
                print("Tiền Thắng : +{}$".format(tienthang))
                print("====================")
                # saved số dư
                with open('assets/xu.txt', 'w') as save_coins:
                    save_coins.write(so_du1)
                # Create History
                with open('assets/lichsu_xoso.txt', 'r') as read_history:
                    history = read_history.read()

                lich_su_cuoc = f"[-] Cuoc {user_input2},{user_input1},{user_input3},{user_input4},{user_input5}, So Tien Cuoc : {tien_cuoc1}$, ket Qua : {giai_dac_biet}, Tien Thang : +{tienthang}$"
                with open('assets/lichsu_xoso.txt', 'w') as historys:
                    data = f"""{history}
{lich_su_cuoc}"""
                    historys.write(data)

            if user_input2 == giai_dac_biet:
                print("===================")
                print("Bạn Đã Trúng Giải")
                print("Phiên : #{}".format(phien))
                print("Số Chọn Cược : {}, {}, {}, {}, {}".format(user_input1, user_input2, user_input3, user_input4, user_input5))
                print("Số Trúng : {}".format(giai_dac_biet))
                print("Tiền Cược : {}$".format(tien_cuoc1))
                tien_thang = int(tien_cuoc * 2 * 60 - (tien_cuoc * 10 / 100))
                tienthang = "{:,}".format(tien_thang)
                so_du1 = str(so_du_hien_tai + tien_thang)
                print("Tiền Thắng : +{}$".format(tienthang))
                print("====================")
                # saved số dư
                with open('assets/xu.txt', 'w') as save_coins:
                    save_coins.write(so_du1)
                # Create History
                with open('assets/lichsu_xoso.txt', 'r') as read_history:
                    history = read_history.read()

                lich_su_cuoc = f"[-] Cuoc {user_input2},{user_input1},{user_input3},{user_input4},{user_input5}, So Tien Cuoc : {tien_cuoc1}$, ket Qua : {giai_dac_biet}, Tien Thang : +{tienthang}$"
                with open('assets/lichsu_xoso.txt', 'w') as historys:
                    data = f"""{history}
{lich_su_cuoc}"""
                    historys.write(data)

            if user_input3 == giai_dac_biet:
                print("===================")
                print("Bạn Đã Trúng Giải")
                print("Phiên : #{}".format(phien))
                print("Số Chọn Cược : {}, {}, {}, {}, {}".format(user_input1, user_input2, user_input3, user_input4, user_input5))
                print("Số Trúng : {}".format(giai_dac_biet))
                print("Tiền Cược : {}$".format(tien_cuoc1))
                tien_thang = int(tien_cuoc * 2 * 60 - (tien_cuoc * 10 / 100))
                tienthang = "{:,}".format(tien_thang)
                so_du1 = str(so_du_hien_tai + tien_thang)
                print("Tiền Thắng : +{}$".format(tienthang))
                print("====================")
                # saved số dư
                with open('assets/xu.txt', 'w') as save_coins:
                    save_coins.write(so_du1)
                # Create History
                with open('assets/lichsu_xoso.txt', 'r') as read_history:
                    history = read_history.read()

                lich_su_cuoc = f"[-] Cuoc {user_input2},{user_input1},{user_input3},{user_input4},{user_input5}, So Tien Cuoc : {tien_cuoc1}$, ket Qua : {giai_dac_biet}, Tien Thang : +{tienthang}$"
                with open('assets/lichsu_xoso.txt', 'w') as historys:
                    data = f"""{history}
{lich_su_cuoc}"""
                    historys.write(data)
            if user_input4 == giai_dac_biet:
                print("===================")
                print("Bạn Đã Trúng Giải")
                print("Phiên : #{}".format(phien))
                print("Số Chọn Cược : {}, {}, {}, {}, {}".format(user_input1, user_input2, user_input3, user_input4, user_input5))
                print("Số Trúng : {}".format(giai_dac_biet))
                print("Tiền Cược : {}$".format(tien_cuoc1))
                tien_thang = int(tien_cuoc * 2 * 60 - (tien_cuoc * 10 / 100))
                tienthang = "{:,}".format(tien_thang)
                so_du1 = str(so_du_hien_tai + tien_thang)
                print("Tiền Thắng : +{}$".format(tienthang))
                print("====================")
                # saved số dư
                with open('assets/xu.txt', 'w') as save_coins:
                    save_coins.write(so_du1)
                # Create History
                with open('assets/lichsu_xoso.txt', 'r') as read_history:
                    history = read_history.read()

                lich_su_cuoc = f"[-] Cuoc {user_input2},{user_input1},{user_input3},{user_input4},{user_input5}, So Tien Cuoc : {tien_cuoc1}$, ket Qua : {giai_dac_biet}, Tien Thang : +{tienthang}$"
                with open('assets/lichsu_xoso.txt', 'w') as historys:
                    data = f"""{history}
{lich_su_cuoc}"""
                    historys.write(data)

            if user_input5 == giai_dac_biet:
                print("===================")
                print("Bạn Đã Trúng Giải")
                print("Phiên : #{}".format(phien))
                print("Số Chọn Cược : {}, {}, {}, {}, {}".format(user_input1, user_input2, user_input3, user_input4, user_input5))
                print("Số Trúng : {}".format(giai_dac_biet))
                print("Tiền Cược : {}$".format(tien_cuoc1))
                tien_thang = int(tien_cuoc * 2 * 60 - (tien_cuoc * 10 / 100))
                tienthang = "{:,}".format(tien_thang)
                so_du1 = str(so_du_hien_tai + tien_thang)
                print("Tiền Thắng : +{}$".format(tienthang))
                print("====================")
                # saved số dư
                with open('assets/xu.txt', 'w') as save_coins:
                    save_coins.write(so_du1)
                # Create History
                with open('assets/lichsu_xoso.txt', 'r') as read_history:
                    history = read_history.read()

                lich_su_cuoc = f"[-] Cuoc {user_input2},{user_input1},{user_input3},{user_input4},{user_input5}, So Tien Cuoc : {tien_cuoc1}$, ket Qua : {giai_dac_biet}, Tien Thang : +{tienthang}$"
                with open('assets/lichsu_xoso.txt', 'w') as historys:
                    data = f"""{history}
{lich_su_cuoc}"""
                    historys.write(data)
            else:
                print("===================")
                print("Chúc Bạn May Mắn Lấn Sau")
                print("Phiên : #{}".format(phien))
                print("Số Chọn Cược : {}, {}, {}, {}, {}".format(user_input1, user_input2, user_input3, user_input4, user_input5))
                print("Số TB Trúng : {}".format(giai_dac_biet))
                print("Tiền Cược : {}$".format(tien_cuoc1))
                so_du1 = str(so_du_hien_tai - tien_cuoc)
                print("Tiền Thắng : -{}$".format(tien_cuoc1))
                print("====================")
                # saved số dư
                with open('assets/xu.txt', 'w') as save_coins:
                    save_coins.write(so_du1)
                # Create History
                with open('assets/lichsu_xoso.txt', 'r') as read_history:
                    history = read_history.read()

                lich_su_cuoc = f"[-] Cuoc {user_input2},{user_input1},{user_input3},{user_input4},{user_input5}, So Tien Cuoc : {tien_cuoc1}$, ket Qua : {giai_dac_biet}, Tien Thang : -{tien_cuoc1}$"
                with open('assets/lichsu_xoso.txt', 'w') as historys:
                    data = f"""{history}
{lich_su_cuoc}"""
                    historys.write(data)
            print("Bắt Đầu Phiên Mới")
            time.sleep(6)
        usr()