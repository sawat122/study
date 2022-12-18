""" 
Bu projede ise 4 tane sınıfı oluşturun.
Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf 
olacak.
Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak.
Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. 
Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. 
Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.
"""

import time

class Animals():
    
    def __init__(self,name,types,colors,feet,habitat,act):
        
        self.name=name
        self.types=types
        self.colors=colors
        self.feet=feet
        self.habitat=habitat
        self.act=act
    
    def __str__(self):
        return "Name: {}\nTypes: {}\nColors: {}\nNumber of feet: {}\nHabitat: {}\nAct: {}".format(self.name,self.types,self.colors,self.feet,self.habitat,self.act)
    
    
class  Dogs(Animals):
    def __init__(self, name, types, colors, feet, habitat, act,nutrition):
        super().__init__(name, types, colors, feet, habitat, act)
        
        
        self.nutrition=nutrition
        
    def __str__(self):
        return super().__str__() + "\nDiet: {}".format(self.nutrition)
        
    

class  Birds(Animals):
    
    def __init__(self, name, types, colors, feet, habitat, act,mouth_shape,movement_limbs):
        super().__init__(name, types, colors, feet, habitat, act)
        
        self.mount_shape=mouth_shape
        self.movement_limbs=movement_limbs
    
    def __str__(self):
        return super().__str__() +"\nMouth shape: {}\nMovement limbs: {}".format(self.mount_shape,self.movement_limbs)
    
class Horses(Animals):
    
    def __init__(self, name, types, colors, feet, habitat, act,place_in_life):
        super().__init__(name, types, colors, feet, habitat, act)
        
        self.place_in_life=place_in_life
    def __str__(self):
        return super().__str__() + "\nPlace in life: {}".format(self.place_in_life)

dog =Dogs("Shadow","Siberian Husky","White",4,"Pets","Active movement","Carnivorous")

bird=Birds("Blues","Canary","Yellow",2,"Pets","Active movement","Beak","Wings")

horse=Horses("No information","Yılkı Horses","Black",4,"Wild","Active movement","Plains")

print("""
      
      Hello ,Welcome
      
      Animal App
      
      1)Information for dog
      
      2)Information for bird
      
      3)Information for horse
      
      Select 'q' to exit the application...
      """)

while True:
    
    process=input("Select the action: ")
    if (process == "q"):
        
        print("Exiting the application...")
        time.sleep(1)
        break
        
    elif (process == "1"):
        print("Loading information for Dog ...")
        time.sleep(1)
        print(dog)
        
    
    elif (process== "2"):
        print("Loading information for Bird...")
        time.sleep(1)
        print(bird)
        
    elif (process == "3"):
        print("Loading information for Horse...")
        time.sleep(1)
        print(horse)
    else:
        print("""The operation you entered is incorrect...
Change Your Transaction!""")
