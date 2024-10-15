# file input output in python
#open file and read
f = open("demo.txt", "r")
data = f.read()   #data = f.read(4)-- you can give a parameter also
print(data)
f.close()  # it is important to close the file

#open and write
f = open("demo.txt", "w")
f.write("hello my name is shubhi") #overwrite file
f.close()

#open and appned data in file
f = open("demo.txt", "a")
f.write("\ni am leaning python")
f.write("\ni am leaning php")
f.write("\ni am from kanpur") # add data in last
f.close()

#open and read line by line data in file
f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 =  f.readline()
print(line3)
line4 =  f.readline()
print(line4)
f.close()

#creating autometic file which is not exists
f = open("sample.txt", "w")
f.write("hello this is a sample file. you can open file in direct write mode with file name that you want to create")
f.close()



# with syntax...
with open("sample.txt", "a") as f:
    f.write("\nadd new data in this file")

with open("sample.txt" , "r") as f: #there is no need to use f.close().
    data = f.read()
    print(data)


# Delete file...using os module
# first create..
with open("n_file.txt", "w") as f:
    f.write("this is a new file")

# now delete..
import os
os.remove("n_file.txt")     



# practice questions...
# Q-1. create a new file "practice.txt" an add some data.
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I/O\n")
    f.write("using java.\nI line programming in java.")

# Q-2. WAF that replace all occurancess of "java" with "python" in above file.
with open("practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# Q-3. Search if the word "learning" in data exist or not.
word = "learning"
with open("practice.txt" ,"r") as f:
    data = f.read()
    if(word in data):
        print("found")
    else:
        print("not found")   

# Q-4. WAP to find in which line of the file does the word "learning" occure first. print -1 if word not found
word ="huu"
data = True
line_no = 1
with open("practice.txt", "r") as f:
    while data:
        data = f.readline()
        if (word in data):
            print(line_no)
            break
        line_no+=1
    else:
        print(-1)

# Q-5. From a file containing numbers seperated by comma, print the count of even numbers.
with open("practice.txt", "w") as f:
    f.write("1 , 3, 44, 12, 10, 34, 33")

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            count+=1
print(count)            

