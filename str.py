#Strings in python
str = "hello", "hiii" #store multiple strings in single str
#escape sequance character
str1 = "my mother's name is mother.\nshe is very sweet."
str2 = "my mother's name is mother.\tshe is very sweet."
str3 =  "my mother's name is mother.she is very \"sweet\"."
str4 = "my name is shubhi \r i am good at frontend"
str5 = "my name is shubhi \\ i am good at frontend"
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)


#concatinate two strings with space between
str1 ="apna"
str2 = "university"
final_str = str1 + " " + str2
print(final_str)

# find length of string
print(len(final_str))

#Strings functions
str = "he is a coder. i am also a coder"
print(str.endswith("er")) # return boolean value
print(str.capitalize())
print(str.replace("he","she"))
print(str.find("a")) #fisrt time exist word index
print(str.count("coder"))

name = " Shubhi Awasthi"
print(name.strip()) #remove white space from starting

name = "Shubhi Awasthi"
check_data = "bh" in name #check given string is present 
print(check_data)   

name = "Shubhi Awasthi"
check_data = "bh" not in name #check given string is not present
print(check_data)

#indexing
str = "apna_university"
print(str[3])
# can not change index value because strings are immutable in python
#str[1] = "3"

#slicing in strings
print(str[1:4])
print(str[:5])
print(str[1:])

#negative slicing index
str = "apple" #index -1 -2 -3 -4 -5 from right
print(str[-3:-1])

#concatinate strings with integers using formate() method
age = 24
txt = "my name is something & i am {} ."
print(txt.format(age))

#formate method takes unlimted no. of arguments
quantity = 3
item_no = 456
price = 49.99
my_order = "i want {} pieces of item {} for {} dollers"
my_order = "i want {2} pieces of item {0} for {1} dollers" #change value according index
print(my_order.format(quantity, item_no, price)) #arguments folllow index
