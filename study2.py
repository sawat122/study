""""Atm Programı"""

print("""
 ************************************
     ATM Makinesine Hoşgeldiniz!!
     
İşlemler;
1)Bakiye Sorgulama
2)Para Yatırma
3)Para Çekme
Programdan çıkmak için 'q' ya basın.
 ************************************
      """)
bakiye =1000
while True:
    işlem = input("İşemi seçiniz: ")
    
    if işlem == 'q':
        print("Yine Bekleriz")
    elif işlem =='1':
        print("Bakiyeniz {} tl dir".format(bakiye))
    elif işlem == '2':
        miktar = int(input("Miktar giriniz: "))
        bakiye += miktar
    elif işlem == '3':
        miktar = int(input("Miktar Giriniz: "))
        if bakiye - miktar < 0:
            print("Böyle bir miktar çekemezsiniz...")
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem....")
