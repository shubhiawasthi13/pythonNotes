# variable declartion
name ="kratika"
age = 24
price = 2000.00
print("my name is : ", name)
print("my age is : ", age, "years old")
# check data type
print(type(age))

#Expression Execution
a = 2
b = 3
txt = "@"
print(a*txt*b)# output: @@@@@@

a = "2"
b = 3
txt = "@"
print((a+txt)*b)# output: 2@2@2@

a = 8
b = 5
c = 2
print(a+b*c)

a = 10
b = 5.0
print(a*b) #output:50.0

a = 10
b = 5
print(a/b)#output: 2.0

a = 1.5
b = 3
print(a//b) #output: 0.0

a = 12
b = 5
print(a//b) #output: 2

a = -12
b = 5
print(a//b) #output: -3

a = 15
b = -2
print(a%b) #output: -1

print(not True)
print(not False)
print(False and True)#output: false
print(True and False)#output: false
print(False and False)#output: false
print(True and True) #output: true

print(False or True)#output: true
print(True or False)#output: true
print(False or False)#output: false
print(True or True) #output: true

# Input in python
name = input("name : ")
age = int(input("age : "))
price = float(input("price : "))
print(name)
print(age)
print(price)
 
#typeconverstion and type casting 
age = 30 # typeconverstion
print(type(age))

num1 = int(input("write a num1 : "))
num2 = int(input("write a num2 : ")) #typecasting
sum = num1 + num2
print(sum)

#Conditional Statements
light = input("Light : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")    
elif(light == "green"):
    print("go")
else:
    print("light is broken")    

#Single line if/ternary operator
food = input("food : ")
eat = "yes" if food == "cake" else "no"
print("eat "+eat)
 
 #short way
food = input("food : ")
print("sweet") if food == "cake" or food == "jlebi" else print("nosweet")
