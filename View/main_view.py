from View.user_view import menu_user
from View.admin_view import login_admin
import os
os.system("cls")

def welcome():
    print("""
===================================================================
||                                                               ||
||         Selamat Datang di Layanan Informasi Tempat Wisata     ||
||                    di Kalimantan Timur                        ||
||                                                               ||
===================================================================
      < Jelajahi berbagai pesona tempat wisata yang memukau! >
""")

def MainProgram():
    os.system("cls")
    welcome()
    while True :
        try :
            print("+--------------------------------------+")
            print("|             LOGIN SEBAGAI            |")
            print("+--------------------------------------+")
            print("|             1. Pengunjung            |")
            print("|             2. Admin                 |")
            print("|             3. Keluar                |")
            print("+--------------------------------------+")
            user = str(input("Silahkan pilih role anda (1/2/3): "))
            if user == "1":
                os.system("cls")
                menu_user()
                break
            elif user == "2":
                os.system("cls")
                login_admin()
                break
            elif user == "3":
                print("========================================================")
                print("||    Terima kasih telah menggunakan layanan kami!    ||")
                print("||                     Sampai Jumpa!                  ||")
                print("========================================================")
                break
            else:
                os.system("cls")
                print('Opsi tidak tersedia')

        except KeyboardInterrupt:
            print('Terjadi kesalahan!')
            break
