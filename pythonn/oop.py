class Student:
    # constructor
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    # method
    def display(self):
        print(self.first_name,self.last_name)


my_student=Student('John','Smith')
my_student.display()
my_student2=Student('Eric','Were')
my_student2.display()
my_student3=Student('Harrison','Wells')
my_student3.display()
my_students4=Student('Oprah','Orneill')
my_students4.display()
my_students5=Student('Anita','Gibson')
my_students5.display()