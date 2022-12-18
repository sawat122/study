# Kullanıcı Giriş örneği

print("""
 *******************************
    Kullanıcı Girişi Programı
 *******************************
    """)

username = "zehra"

parola = "1234"

hak = 3
nameDogru = False


for i in range(hak):
    if not nameDogru:
        name = input("Kullanici adınızı giriniz: ")
    pw = input("Parolanızı giriniz: ")
    if name == username:
        nameDogru = True
        if pw == parola:
            print("Giriş Başarılı!!")
            break

        else:
            hak -= 1
            print("Parola Hatalı!!Kalan hakkınız:{}".format(hak))
            continue
    else:
        hak -= 1
        print("Kullanıcı adı hatalı!! Kalan hakkınız: {}".format(hak))
        
    if hak == 0:
        print("Giriş Hakkınız Bitti...")
        break
