"""
Kumanda sınıfı geliştirme

"""

import random
import time

class Kumanda():
    
    
    def __init__(self,tv_durum="Kapalı",tv_ses= 0,kanal_listesi =["Trt"],kanal = "Trt",uygulama_listesi=["Netflix"],uygulama= "Netflix"):
        
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal 
        self.uygulama_listesi =uygulama_listesi
        self.uygulama = uygulama 
        
    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık....")
            
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum = "Açık"
        
    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon Zaten Kapalı....")
            
        else:
            print("Televizyon Kapanıyor...")
            self.tv_durum= "Kapalı"
            
    def ses_ayarları(self):
        
        while True:
            cevap =input("Sesi Azalt:'<'\nSesi Artır: '>'\nÇıkış: çıkış\n")
            
            if cevap == "<" :
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 31:
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break               
                
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        
        self.kanal_listesi.append(kanal_ismi)
        
        print("Kanal Eklendi...")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki Kanal:",self.kanal)
        
    def uygulama_ekle(self,uygulama_ismi):
        print("Uygulama ekleniyor...")
        time.sleep(1)
        
        self.uygulama_listesi.append(uygulama_ismi)
        
        print("Uygulama Eklendi...")
    def rastgele_uygulama(self):
        rast =random.randint(0,len(self.uygulama_listesi)-1)
        self.uygulama=self.uygulama_listesi[rast]
        print("Şu anki Uygulama: ",self.uygulama)
        
    
    
    def __len__(self):
        
        return len(self.kanal_listesi)
        
        
    def __str__(self):
        
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\nUygulama Listesi: {}\nŞu anki Uygulama: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal,self.uygulama_listesi,self.uygulama)
    
    
print("""
      Televizyon Uygulaması
      
      1.Tv Aç
      
      2.Tv Kapat
      
      3.Ses Ayarları
      
      4.Kanal Ekle
      
      5.Kanal Sayısını Öğrenme
      
      6.Rastgele Kanala Geçme
      
      7.Uygulama Ekle
      
      8.Rastgele Uygulamaya Geçme
      
      9.Tv Bilgileri
      
      Çıkmak için 'q' ya basın .
      """)

kumanda = Kumanda()




while True:
    işlem =input("İşlemi Seçiniz: ")
    
    if işlem == "q":
        print("Program Sonlandırılıyor...")
        break
    
    elif işlem == "1":
        kumanda.tv_ac()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem== "4":
        kanal_isimleri =input("Kanal isimlerini ',' ile ayırarak girin: ")
        
        kanal_listesi =kanal_isimleri.split(",")
        for  eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
            
    elif işlem == "5":
        print("Kanal Sayısı:",len(kumanda))
        
    elif işlem == "6":
        kumanda.rastgele_kanal()
        
    elif işlem =="7":
        uygulama_isimleri=input("Uygulama isimlerini ',' ile ayırarak girin: ")
        
        uygulama_listesi =uygulama_isimleri.split(",")
        
        for ekle in uygulama_listesi:
            kumanda.uygulama_ekle(ekle)
    
    
    elif işlem == "8":
        kumanda.rastgele_uygulama()
    
    elif işlem == "9":
        
        print(kumanda)
    else:
        print("Geçersiz işlem....")
