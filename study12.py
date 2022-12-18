"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.
liste = ["345","sadas","324a","14","kemal"]
Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
Bunu yaparken try,except bloklarını kullanmayı unutmayın.
"""



liste = ["345","sadsf","14","Kemal","sdsf","22"]
for i in liste:
    try:
        i=int(i)
        print(i, end=" ")
    except:
        pass
