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