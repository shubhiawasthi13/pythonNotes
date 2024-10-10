# functions in python
def calc_sum(a=5, b=5): # def- keyword | a and b are parameters or variable | pass default value
    sum = a + b
    return print(sum)

calc_sum(60, 78) #pass arguments or variable values
calc_sum()  #default value executed


# practice Questions...

# Q-1. WAF to print the length of a list.
num_list = [2,4,5,6,7,8,9,12]
def list_len(list):
    return print(len(list))

list_len(num_list)

# Q-2. WAF to print the elements of a list in a single lines.
num_list = [2,4,5,6,7,8,9,12]
def print_list(list):
    for item in list:
        print(item , end =" ")

print_list(num_list)

# Q-3. WAF to find factorial of n.

def find_fact(n):
       fact = 1
       for i in range(1, n+1):
           fact*=i
       return print(fact)  
find_fact(5)            


# Q-4. WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =" ,inr_val, "INR")

converter(1)    




# Function *RECURSION*
def show(n):
    if(n == 0): #Base case
        return
    print(n)
    show(n-1)
    print("end")     

show(5) #print 5 to 1 nums

# factorial of n number
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n* fact(n-1)   

print(fact(3))  

# sum of n number
def calc_sum(n):
    if(n == 0):
        return 0
    else:
        return n + calc_sum(n-1)   

print(calc_sum(5))  

# Write a recursive function to print all elements in a list.
def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

user_details = ["name : kamya" ,"age : 22" ,"user-id : 223344"]    
print_list(user_details)