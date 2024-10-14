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
