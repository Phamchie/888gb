import time
import os
def kichhoat_otp():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
.------..------..------..------..------.
|8.--. ||8.--. ||8.--. ||G.--. ||B.--. |
| :/\: || :/\: || :/\: || :/\: || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() |
| '--'8|| '--'8|| '--'8|| '--'G|| '--'B|
`------'`------'`------'`------'`------'
""")
    phone = int(input("Nhập Số Điện Thoại Vừa Lấy Code : "))
    # check 
    with open('otp_code/phone/sdt.txt', 'r') as phones:
        phones = phones.read()
        phones = int(phones)

    if phone == phones:
        codes = int(input("Nhập Code để Xác Nhận : "))
        # check code
        with open('otp_code/code.txt', 'r') as code:
            code = code.read()
            code = int(code)
        
        if codes == code:
            print("============================")
            print("Kích Hoạt Thành Công")
            print("Tài Khoản Của Bạn Được")
            print("Nhận 100,000đ về TK")
            print("Chúc Bạn Chơi Game Vui Vẻ")
            print("============================")
            def nhan_thuong():
                with open('assets/xu.txt', 'r') as so_du:
                    so_du = so_du.read()
                    so_du1 = int(so_du)
                phan_thuong = 100000
                tong = str(so_du1 + phan_thuong)

                with open('assets/xu.txt', 'w') as nhan_thuong:
                    nhan_thuong.write(tong)
            nhan_thuong()

            def reset_code():
                code222 = "0"
                with open('otp_code/code.txt', 'w') as resetcode:
                    resetcode.write(code222)
            reset_code()

        else:
            print("Code Không Đúng, Hoặc Không Tồn Tại")
    else:
        print("Không có dữ liệu về số điện thoại này")
        print("Vui Lòng kiểm tra lại")
        exit()