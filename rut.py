import random

code_text = ["AWNP", "BWMAN", "VMCHA", "EMNVW", "FTYABC", "MNVGS", "NAGVDM", "M"]
code_text = random.choice(code_text)
code_num = random.randint(1000000000, 99999999999)

def rut_tien():
    with open('assets/xu.txt', 'r') as so_du5:
        so_du5 = int(so_du5.read())
    rutt = int(input('Nhập Số Tiền Rút : '))
    if rutt > so_du5:
        print("Bạn Không Đủ Số Dư Để thực hiện giao dịch rút tiền")
        exit()
    rut1 = int(rutt)
    rutt1 = "{:,}".format(rut1)
    bank = input("Nhập Tên Ngân Hàng : ")
    stk = input("Nhập Số Tài Khoản : ")
    
    with open('assets/xu.txt', 'r') as so_du:
        so_du = int(so_du.read())
        so_du = str(so_du - rutt)

    with open('assets/xu.txt', 'w') as so_du1:
        so_du1 = so_du1.write(so_du)
    
    print("""
===========================
STK : {}
NGÂN HÀNG : {}
SỐ TIỀN RÚT : {}
NỘI DUNG : {}{}
===========================
""".format(stk, bank, rutt1, code_text, code_num))

    print("""
==========================
    HƯỚNG DẪN CÁCH RÚT
==========================
1. Sau Khi Điền Đủ Thông Tin
Và tạo lịch sử rút, vui lòng 
chụp lại lịch sử rút và gửi qua
Telegram : @TranHoangAnh006 để
nhận được tiền một cách nhanh nhất
===========================
   """)