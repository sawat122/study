"""
Şimdi de geometrik şekil hesaplama işlemi yapalım.
İlk olarak kullanıcıdan üçgenin mi dörtgenin mi 
tipini bulmak istediğini sorun.Eğer kullanıcı 
"Dörtgen" cevabını verirse , 4 tane kenar isteyip bu 
dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir 
dörtgen mi olduğunu bulmaya çalışın.Eğer kullanıcı 
"Üçgen" cevabını verirse , 3 tane kenar isteyip bu
üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir
üçgen mi olduğunu bulmaya çalışın. Eğer verilen 
kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen 
belirtmiyor" şeklinde bir yazı yazın.o"""



print("Seçmek İstediğiniz Geometrik Şekil\n1)Dörtgen\n2)Üçgen")

sec =int(input("İstediğniz şekil için değer belirleyin: "))

if sec == 1:
    a =int(input("Bir sayı giriniz: "))
    b =int(input("Bir sayı giriniz: "))
    c =int(input("Bir sayı giriniz: "))
    d =int(input("Bir sayı giriniz: "))
    if a ==b and a == c and a == d:
            print("KARE'dır")
    elif a == c and b==d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")
else:
    x =int(input("Bir sayı giriniz: "))
    y =int(input("Bir sayı giriniz: "))
    z =int(input("Bir sayı giriniz: "))
    
    if abs(y-z)<x:
        if x< abs(y+z):
            print("Üçgen belirtme şartına uyuyor") 
            if x !=y and x !=z and y != z:
                print("Sıradan bir üçgen") 
            if x==y :
                if x==z:
                    print("Eşkenar üçgen")
                else:
                    print("İkizkenar üçgen.")
            
            else:
                if x ==z:
                    print("İkizkenar üçgen.")
        else:
             print("Üçgen belirtme şartına uymuyor.")
    else:
        print("Üçgen belirtme şartına uymuyor.")
