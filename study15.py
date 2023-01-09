"""
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı 
çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını 
hesaplayan bir fonksiyon yazın ve bu listenin her bir 
elemanına bu fonksiyonu uygulayarak ekrana şöyle bir 
liste yazdırın.

         [12, 30, 30, 9]

Not: map() fonksiyonunu kullanmaya çalışın.
"""



liste1=[(3,4),(10,3),(5,6),(1,9)]
liste2=[]
liste3=[]
for i in liste1:
    for j,k in enumerate(i):
        if j %2==0:
            liste2.append(k)
        else:
            liste3.append(k)
print(liste2,liste3)
        
print(list(map(lambda x,y: x*y,liste2,liste3)))
