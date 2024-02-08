import random

code_text = ["AWNP", "BWMAN", "VMCHA", "EMNVW", "FTYABC", "MNVGS", "NAGVDM", "M"]
code_text = random.choice(code_text)
code_num = random.randint(1000000000, 99999999999)

def naps():
    nap_xu = int(input("Nhập Số Tiền Cần Nạp : "))
    nap_xu1 = "{:,}".format(nap_xu)
    print("")
    print(f"Số Tiên Nạp : {nap_xu1}đ")
    print("")
    print("STK : 8800205311040")
    print("CHỦ TK : CHU THI THAM")
    print("Ngân Hàng : Agribank")
    print("Nội Dung : {}{}".format(code_text, code_num))
    print("""
===========================
    Hướng Dẫn Cách Nạp
===========================
1. Sau Khi Bank Vui Lòng Chụp
Lại Bill và gửi cho admin qua
Telegram : @TranHoangAnh006
Để Được Cộng Xu vào Tài Khoản
Sớm Nhất Có Thể

2. Mỗi Lần chuyển khoản, Xin hãy nhập
nội dung được ghi ở phía trên
đó lad mã xác nhận để nạp tiền

LƯU Ý : Nếu Không Điền Nội Dung
bạn sẽ có thể mất tiền oan
và chúng tôi không chịu trách nghiệm
===========================
""")