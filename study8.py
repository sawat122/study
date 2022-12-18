"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu 
sayının okunuşunu bulan bir fonksiyon yazın.
"""

d ={0:" ",1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz"}
k ={1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksan",9:"doksan"}

def okunus(x):
    a =x//10
    b =x % 10
    return k[a] + " " +d[b]
x =int(input("İki basamaklı bir değer:"))
print(okunus(x))
