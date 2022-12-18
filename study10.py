""" 
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler 
ekleyin ve bu class'ı kullanmaya çalışın.
"""
import time

class Computer_class():
    def __init__(self,number_of_people,number_of_computers): 
      self.number_of_people=number_of_people
      self.number_of_computers=number_of_computers
    def __str__(self):
        return "Number of People: {}\nNumber of computers".format(self.number_of_people,self.number_of_computers)


    def balance(self):
        
        if (self.number_of_people<=self.number_of_computers):
            print("Computer are enough...")
        
        elif (self.number_of_people > self.number_of_computers):
            
            a =int(self.number_of_people)-int(self.number_of_computers)
            
            self.number_of_computers += a
            print("Are held...")
            time.sleep(1)
            print("Updated issue: ",self.number_of_computers,"Added: ",a)

computer_class=Computer_class(110,90)
print("""
    Computer Class Welcome
    
    1.Computer Class information
    2.To balance
    
    press 'q' to exit process
""")    
while True:
    process =input("Make your choice..: ")
    if (process== 'q'):
        print("Transaction exited...")
   
    elif (process == "1"):
        
        print("Student: {}\nComputer: {}".format(computer_class.number_of_people,computer_class.number_of_computers))
    
    elif(process=="2"):
        computer_class.balance()
        
    else:
        print("The operation you want to perform could not be found....")
        break
