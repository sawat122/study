"""
Elinizden her bir elemanı 3'lü bir demet olan bir liste 
olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen 
olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen
belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

Not:filter() fonksiyonunu kullanmaya çalışın
"""


def ucgen_mi(h):
     
     if (abs(h[0]+h[1])> h[2] and abs(h[0]+h[2])>h[1] and abs(h[1]+ h[2])>h[0]):
          return True
     else:
          return False
s =[(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(ucgen_mi,s)))
