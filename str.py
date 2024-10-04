#Strings in python
str = "hello", "hiii" #store multiple strings in single str
#define string with next line using escape sequance character
str = "my mother's name is mother.\nshe is very sweet."
print(str)

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

