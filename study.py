
"""Hesap Makinesi örneği if, elif, else kullanarak."""

print("******************************\nHesap Makinesi Programı\n1)Toplama(+)\n2)Çıkarma(-)\n3)Çarpma(x)\n4)Bölme(/)\n******************************")

a =int(input("Bir sayı giriniz:"))
b=int(input("Bir sayı giriniz: "))
işlem=input("Yapmak istediğiniz işlem sembolünü giriniz: ")

if işlem == "+":
    print("{} ile {} in toplamı {}".format(a,b,a+b))   
elif işlem == "-":
    print("{} ile {} in çıkarımı {}".format(a,b,a-b))
elif işlem == "x":
    print("{} ile {} in çarpımı {}".format(a,b,a*b))
elif işlem == "/":
    print("{} ile {} in bölümü {}".format(a,b,a/b))
else:
    print("Girdiğiniz ifade hatalı!")
