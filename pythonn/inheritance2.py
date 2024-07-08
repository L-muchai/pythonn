class Person:
    def __init__(self, first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print_name(self):
        print(f'My name is {self.first_name} {self.last_name} and I am {self.age} years old.')
# my_self=Person('ken','Marrie',34)
# my_self.print_name()

class Student(Person):
    def __init__(self, first_name,last_name,age):
        super().__init__(first_name,last_name,age)
my_self=Student('ken','Marrie',34)
my_self.print_name()
my_self2=Student('Maria','Thompson',56)
my_self2.print_name()
my_self3=Student('Thomas','Lumbrey',45)
my_self3.print_name()