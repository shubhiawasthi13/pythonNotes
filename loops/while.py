# while loop in python

i = 1 #initialization
while i <=5: #condition
    print("hello",i)  #work
    i+=1              #updation
print("end loop")

#practice questions
# print num 1 to 100.
i = 1
while i <= 100:
    print(i)
    i+=1

# print num 100 to 1.
i = 100
while i >= 1:
    print(i)
    i-=1

# print the multipication table of a num n.
i = 1
num = int(input("write a number: "))
while i <=10:
    print(i*num)
    i+=1

# print the elements of the following list using a loop
nums = [1, 6, 7, 55, 34, 2, 67]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx+=1

# Search for a number x in tuple using loop
tup = (1, 6, 7, 55, 34, 2, 7, 67)
idx = 0
x = 7
while idx < len(tup):
    if(tup[idx] == x):
        print("found at idx: " , idx)
    else:
        print("finding...")
    idx+=1    

# Break....
tup = (1, 6, 7, 55, 34, 2, 7, 67)
idx = 0
x = 7
while idx < len(tup):
    if(tup[idx] == x):
        print("found at idx: " , idx)
        break # loop terminate from here
    else:
        print("finding...")
    idx+=1  
print("end loop")

#continue.....
tup = (1, 6, 7, 55, 34, 2, 7, 67)
idx = 0
while idx < len(tup):
    if(tup[idx] == 7):
        idx+=1
        continue #skip and countine itration
    print(tup[idx])
    idx+=1    
print("end loop")

# write a program to find odd num using loop
i = 1 
while i <= 50:
    if(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1
    # write a program to find even num using loop
i = 1 
while i <= 50:
    if(i%2 != 0):
        i+=1
        continue
    print(i)
    i+=1


#  write a program to find odd num in given list using loop
num_list = [2,45,34,66,33,12,13,15]
idx = 0
while idx < len(num_list):
    if(num_list[idx]%2 == 0):
        idx+=1
        continue
    print(num_list[idx])
    idx+=1