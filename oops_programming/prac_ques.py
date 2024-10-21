# # oops practice questions
# # Q-1. Define a Circle class to create a circle with radius r using constructor.
# # Define an Area() method of the class which calculates the area of the circle.
# # Define a Parameter() method of the class which allow you to calculat the parameter of the circle.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return (22/7) *self.radius **2    

#     def parameter(self):
#         return 2 * (22/7) *self.radius
    
# C1 = Circle(21)
# print(C1.area())    
# print(C1.parameter())

# # Q-2 Define a employee class with attributes and create a method to show the employee details.
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
#     def showDetails(self):
#         print("role: ", self.role)
#         print("deparment: ", self.dept)
#         print("salary: ", self.salary)

# E1 = Employee("accountant","Fainanace","70,000")
# print(E1.showDetails())

# # Q-3 Create an Engineer class that inherit properties from employee and have some attribute name and age.
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "80,000")

# eng1 = Engineer("hardik panday", 40)
# print("name: ",eng1.name)
# print("age: ",eng1.age)
# eng1.showDetails()      


# Q-4 Create a class order which store item and price.
# use dunder function __gt__() to convey that......order1 > order2 if price of order1 > order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, odr2):
        return self.price >odr2.price

ord1 = Order("chips",90)
odr2 = Order("tea", 50)
print(ord1>odr2)        