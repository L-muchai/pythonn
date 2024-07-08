# CREATE A CLASS CALLED CARS WITH THE FOLLOWING ATTRIBUTES
# MODEL, YEAROFMANUFACTURE,TYPE,COLOUR
#
# CREATE A METHOD TO PRINT
# "MY DREAM CAR IS...MANUFACTRED IN...BEING A ...TYPE... IN COLOUR..."
#
# INITIALIZE WITH ATLEAST 5 OBJECTS

class Cars:
    def __init__(self,model,yearofmanufacture,type,colour):
        self.model=model
        self.yearofmanufacture=yearofmanufacture
        self.type=type
        self.colour=colour

    def display(self):
        print(f"My dream car is {self.model} manufactured in {self.yearofmanufacture} being a {self.type} type  {self.colour} in colour")

my_Cars=Cars('Toyota',1989,'Premio','blue')
my_Cars.display()
my_Cars2=Cars('Toyota',1890,'Harrier','red')
my_Cars2.display()
my_Cars3=Cars('Bima',1789,'e-200','Black')
my_Cars3.display()
my_Cars4=Cars('Mazda',2013,'CX-5','beige')
my_Cars4.display()
my_Cars5=Cars('Honda',1987,'CR-V','Lush green')
my_Cars5.display()