"""  
 Etkileşimli çalışarak kullanıcıdan sayılar alan ve aldığı sayıların 
 karesini ekrana basan bir program yazalım. Boş satır okuduğunda 
 program sonlansın.
"""
a = input("Enter a number:")
b = input("Enter a number: ")
try:
    a =int(a)
    b =int(b)
    
    square=a**b
    print("Square: ",square)
    
except :
    print("Hata bulunmuştur...")
