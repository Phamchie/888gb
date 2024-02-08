import random
import os
import time
def creator_otp():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
.------..------..------..------..------.
|8.--. ||8.--. ||8.--. ||G.--. ||B.--. |
| :/\: || :/\: || :/\: || :/\: || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() |
| '--'8|| '--'8|| '--'8|| '--'G|| '--'B|
`------'`------'`------'`------'`------'
""")
    random_code = random.randint(100000, 999999)
    codes = str(random_code)
    number = input("Số Điện Thoại : ")
    print("=================================================")
    print("Đang Tạo Code OTP cho Số Điện Thoại : {}".format(number))
    print("Code Của Bạn Là : {}".format(random_code))
    print("=================================================")

    def save_data():
        with open('otp_code/code.txt', 'w') as code:
            code.write(codes)
        def save_phone():
            with open('otp_code/phone/sdt.txt', 'w') as phone:
                phone.write(number)
        save_phone()
    save_data()
