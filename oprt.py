# #operators in python
#Arithmetic operators
num1 = int(input("write first num : "))
num2 = int (input("write second num: "))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

#Relational/ Comparison operators
A = 5
B = 7
print(A==B)
print(A!=B)
print(A>B)
print(A<B)
print(A>=B)
print(A<=B)

#Assignment operators
A = 10
#perform all operator like that
A+=5
print(A)

#Logical operators
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

#practice questions
#wrirte a program to find largest of fourth number
a = int(input("Write first number : "))
b = int(input("Write second number : "))
c = int(input("Write third number : "))
d = int(input("write fourth number : "))

if(a >= b and a >= c and a >= d):
    print("number 1 is the largest number",a)
elif(b >= c and b >= d):
    print("number 2 is the largest number",b)
elif(c >= d):
    print("number 3 is the largest number",c)
else:
    print("number 4 is the largest number",d)       
