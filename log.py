import os

def sessions():
    print("""
.------..------..------..------..------.
|8.--. ||8.--. ||8.--. ||G.--. ||B.--. |
| :/\: || :/\: || :/\: || :/\: || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() |
| '--'8|| '--'8|| '--'8|| '--'G|| '--'B|
`------'`------'`------'`------'`------'
""")
    print(" chào mừng bạn đến với ")
    print("   Game Bài Python")
    print("======================")
    print("1, Đăng Nhập")
    print("2, Đăng Ký")
    print("3, Quên Mật Khẩu")
    print("======================")
    user_choose = input("Vui Lòng Chọn : ")
    if user_choose == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            #check
            def checking():
                username = input("Tên Đăng Nhập : ")
                with open('data/data_info/user.txt', 'r') as usr:
                    usr = usr.read()
                if username == usr:
                    password = input("Mật Khẩu : ")
                    with open('data/data_info/password.txt', 'r') as passwd:
                        passwd = passwd.read()
                    if password == passwd:
                        print("Đăng Nhập Thành Công...")
                    else:
                        print("Sai Mật Khẩu")
                        exit()
                else:
                    print("Sai Tên Đăng Nhập :", username)
                    exit()
            checking()
        except:
            print("Server Database Error")
            print("Không Tìm Thấy Dữ Liệu")
    
    if user_choose == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        def LogUp():
            username = input("Tên Đăng Nhập : ")
            with open('data/data_info/user.txt', 'w') as usern:
                usern = usern.write(username)
            
            password = input("Mật Khẩu : ")
            password2 = input("Nhập Lại Mật Khẩu : ")
            if password2 == password:
                with open('data/data_info/password.txt', 'w') as passwd:
                    passwd = passwd.write(password)
                
                nickname = input("Tên Nhân Vật : ")
                with open('data/data_info/nickname.txt', 'w') as nickn:
                    nickn = nickn.write(nickname)
                
                print("Đăng Ký Thành Công, Vui Lòng Đăng Nhập Lại")
            else:
                print("Mật Khẩu Không Khớp Với Mật Khẩu Trên")
                exit()
        LogUp()
    
    if user_choose == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Vui Lòng Liên Hệ Tele : @TranHoangAnh006 để Được Tư Vấn")
        print("Liên Kết Tư Vấn : https://t.me/TranHoangAnh006")