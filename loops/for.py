#for loops in python
tup = ("appple","orange","banana","guava")
for val in tup:
    print(val)

#break in for loop
tup = ("appple","orange","banana","guava")
for val in tup:
    if(val == "banana"):
       break
    print(val)
    
#continue in for loop
tup = ("appple","orange","banana","guava")
for val in tup:
    if(val == "banana"):
       continue
    print(val)
 
#find a number in tuple
tup = (2,4,5,7,55,33,22)
x = 33
idx = 0
for el in tup:
    if(el == x):
        print("num found at idx :", idx)
    else:
        print("finding...")    
    idx+=1   





# ....//RANGE//....
for el in range(2,10,2): #(start, stop, step)
    print(el)

# print num from 1 to 100
for el in range(1,101):
    print(el)

#print num from 100 to 1
for el in range(100, 0 ,-1):
    print(el)

#find even no. in given range
n = 50 
for el in range(2,n,2):
    print(el)

#print table of n number
n = int(input("write a number: "))
for el in range(1,11):
    print(n*el)

# WAP to sum of natural numbers 
n = 14
sum = 0
for el in range(1,n+1):
    sum+=el
print("sum of number: " ,sum) 

# WAP to factorial of given numbers 
n = 4
fact = 1
for el in range(1,n+1):
    fact*=el
print("fact of number: " ,fact)  




#....//pass statment//....
for el in range(10):
    pass  #used to create empty loop

print("next work...")