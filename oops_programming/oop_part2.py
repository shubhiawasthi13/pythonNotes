# oops programming here //part-2//
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("ajay")
print(s1.name)

#delete class
del s1.name
del s1

#private methods and attributes
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # private attr || only access in class 
    
    def __password_info(self): # private attr || only access in class 
        print("your password is", self.__acc_pass)

    def check_pass(self):
        print("hello this is from abc bank")
        self.__password_info()
        
ac1 = Account("123456", "5gfhh6768")
print(ac1.acc_no)



# inheritane
# single inhe...
class Car:  # parent class
    @staticmethod
    def start():
        print("car staring")
    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(Car): # child class
    def __init__(self, name):
        self.name = name

Car1 = ToyotaCar("fortuner")
print(Car1.name)
print(Car1.start())

# multi-line inhe...
class Car:  # parent class
    @staticmethod
    def start():
        print("car staring")
    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(Car): # child class
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self , type):
        self.type = type

car1 = Fortuner("petrol")
print(car1.type)
print(car1.start())


# multiple inhe...

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# super keyword...
class Car:  # parent class
    def __init__(self ,type):
        self.type = type
    @staticmethod
    def start():
        print("car staring")
    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(Car): # child class
    def __init__(self, name, type):
        super().__init__(type) # access parent methods
        self.name = name

car1 = ToyotaCar("prius", "electric")
print(car1.name)
print(car1.type)

# class method
class Subject:
    name = "python"
    @classmethod
    def change_name(cls,name):
        cls.name = name

S1 = Subject()
print(S1.name)
S1.change_name("PHP")
print(S1.name)

# property Method
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"    
    
stu1 = Student(98, 78, 88)    
print(stu1.percentage)
stu1.chem = 70
print(stu1.percentage)


# Poymorphism...
class Complex: # same operator with different meaning
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real, "i" , "+", self.img, "j")
    
    def __add__(self, num2): # dunder function
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)
    
    def __sub__(self, num2): # dunder function
        new_real = self.real - num2.real
        new_img = self.img - num2.img
        return Complex(new_real, new_img)

num1 = Complex(2,5)
num1.show_number()
num2 = Complex(3,2)
num2.show_number()

add_complex = num1 + num2
add_complex.show_number()

sub_complex = num1 - num2
sub_complex.show_number()
