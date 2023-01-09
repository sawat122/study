"""Bir sınıfın harf notlarını hesaplama"""

def not_hesapla(satır):
    
    satır=satır[:-1]
    
    liste =satır.split(",")
    isim =liste[0]
    not1 =int(liste[1])
    not2 =int(liste[2])
    not3 =int(liste[3])
    son_not =not1 * (3/10) + not2 * (3/10) +not3 * (4/10)
    
    if son_not>= 90:
        harf= "AA"
    elif son_not >=85:
        harf ="BA"
    elif son_not >=80:
        harf ="BB"
    elif son_not >=75:
        harf ="CB"
    elif son_not >=70:
        harf ="CC"
    elif son_not >=65:
        harf ="DC"
    elif son_not >=60:
        harf ="DD"
    elif son_not >=55:
        harf ="FD"
    else:
        harf ="FF"
    return isim + "-------->" + harf + "\n"

def geçen_not(gec):
    gec=gec[:-1]

    


with open("notdosya.txt","r",encoding="utf-8") as file:
    
    
    eklenecekler_listesi =[]
    geçen_listesi=[]
    kalan_listesi=[]
    for  i in file:
        eklenecekler_listesi.append(not_hesapla(i))
        
    print(eklenecekler_listesi)
    
    with open("notlar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)
    with open("gecennot.txt","w",encoding="utf-8") as file3:
        for i in eklenecekler_listesi:
            if int(not_hesapla(satır))>=55:
                geçen_listesi.append(not_hesapla(i))
                file3.write(i)
            
    with open("kalannot.txt","w",encoding="utf-8") as file4:
        for i in eklenecekler_listesi:
            if int(not_hesapla(satır))<55:
                kalan_listesi.append(not_hesapla(i))
                file4.write(i)
