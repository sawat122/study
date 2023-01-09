bölünen = int(input("bölünecek sayı: "))

if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

bölen = int(input("bölen sayı: "))
print(bölünen/bölen)





tr_karakter = "şçğüöıİ"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass

print("Parola kabul edildi!")
"""
Bu kodlar çalıştırıldığında, eğer kullanıcı, içinde Türkçe karakter 
geçen bir parola yazarsa kendisine TypeError tipinde bir hata mesajı 
gösteriyoruz. Eğer kullanıcının parolası Türkçe karakter içermiyorsa 
hiçbir şey yapmadan geçiyoruz ve bir sonraki satırda kendisine ‘Parola
kabul edildi!’ mesajını gösteriyoruz.

"""

giriş = input("Merhaba! Adın ne? ")
if len(giriş) == 0:
    raise AssertionError("İsim bölümü boş.")
print("Hoşgeldiniz.")


"""
assert(idda etmek anlamına gelir) ifadesi aynı zamanda hata yükseltmenin kısa bir yoludur. 
Ancak assert ifadesini kullanarak sadece AssertionError türünde bir 
hata yükseltebiliriz. Normalde raise kullanmamız daha doğru olacaktır.
Dediğimiz gibi assert ifadesi hızlı bir şekilde kodumuzdaki hataları
belirlemek için kullanılır. 

"""

giriş = input("Merhaba! Adın ne? ")
assert len(giriş) != 0 , "İsim bölümü boş."
print("Hoşgeldiniz.")
