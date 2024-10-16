# stating oops programming here //part-1//
# class & onjects..
class Student:   #creating class
    name = "karan"
 
s1 = Student()  # creating object
#print(s1)
print(s1.name)

s2 = Student()  # creating object
print(s1.name)


# # init function or constructor
class Student:
    college_name = "abc college" #class attribute -- no need to create obj
      # default constructer
    def __init__(): 
        pass
     # parameterized constructer
    def __init__(self, name , marks):
        # print (self)       # ref of current obj
        self.name = name  #object attribite
        self.marks = marks #object attribite
          
s1 = Student("karan", 77)
print(s1.name, s1.marks)
print(Student.college_name)
# print(s1)  # at this this is current obj

s2 = Student("aditya", 89)
print(s2.name, s2.marks)
print(Student.college_name)
# print(s2)  # at this this is current obj


# Methods....
class Student:
    #static method
    @staticmethod # decorator == change behave of function
    def hello():
        print("hello")
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    # dynamics methods
    def welcome(self):
        print("welcome student, ", self.name)    

    def get_marks(self):
        print("your marks: ",self.marks)

s1 = Student("karan", 78)
Student.hello()
s1.welcome()
s1.get_marks()

s2 = Student("arnav", 89)
Student.hello()
s2.welcome()
s2.get_marks()


# practice questions...
# Q-1. Create stu. class takes name and marks of 3 subjects as argu. in constr.. then create method to print the aavg of marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("your avg score is :" ,sum/3)   

s1 = Student("riya", [77,88,89])
s1.get_avg()

# Q-2. Create class account with 2 attr. bal and accno.
# create methods for debite , credit and printing balance
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print(amount, "was debited")
        print("total balance: ", self.balance)    

    def credit(self, amount):
        self.balance += amount
        print(amount, "was credited")
        print("total balance: ", self.balance)  

acc1 = Account(10000,12454)
print(acc1.balance)
acc1.credit(1200)
acc1.debit(600)