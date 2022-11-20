print("===========================================")
print("   Selamat Datang di ATM SYAHRUL-GUNAWAN   ")
print("===========================================")
print("                 Pilih option :            ")
print("===========================================")
print("                1. Cek uang                ")
print("                2. Ambil uang              ")
print("                3. Tabung uang             ")
print("===========================================")
option=int(input("Silahkan pilih option :"))
if option==1:
    print("uang kamu berjumlah Rp. 300.000")
elif option==2:
    print("uang kamu berjumlah Rp. 300.000, mau ambil berapa")
    print("1. 100.000")
    print("2. 200.000")
    print("3. 300.000")
    uang_kamu=300000
    option2=int(input("Pilih option :"))
    if option2==1:
        hasil=uang_kamu-100000
        print("uang kamu sekarang berjumlah Rp. :", hasil)
    elif option2==2:
        hasil2=uang_kamu-200000
        print ("uang kamu sekarang berjumlah Rp. :", hasil2)
    elif option2==3:
        hasil3=uang_kamu-300000
        print ("uang kamu sekarang berjumlah Rp. :", hasil3)
    else:
        print("keyword anda salah!")
elif option==3:
    uang_kamu=300000
    print("uang berjumlah Rp. 300.000, mau nabung berapa.?")
    option3=int(input("masukan jumlah uang :"))
    hasil4=uang_kamu+option3
    print("jumlah uang kamu sekarang adalah Rp. :", hasil4)
else:
    print("keyword anda salah, silahkan masukan lagi:")