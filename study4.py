"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendine hariç bölenlereinin toplamı kendine eşitse bu sayı 'mükemmel sayı' denir.
 
Örnek olarak , 6 mükemmel bir sayıdır.(1+2+3 =6)
"""




top = 0
muk = int(input("Bir sayı giriniz: "))
liste = [i for i in range(1,muk) if muk % i == 0]
while True :
    top = sum(liste) #Listenin içindeki değerleri toplamamızı sağlıyor.
    if top == muk:
        print(muk,"mükemmel sayıdır!")
        break
    else:
        print(muk,"mükemmel sayı değildir!")
