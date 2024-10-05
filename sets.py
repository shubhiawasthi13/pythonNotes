# sets in pythond
collection = {1, 2, 5, 7, "hello", 8 } # it store unique value
print(collection)

collection = {1,3,4,5,6,5,5}
print(len(collection)) #does not count dublicate value
print(collection) #remove duplicate value

#create empty set
collection = set()
print(type(collection))

#set methods/functions
collection = {1,3,4,5}

collection.add(7) #add new element
print(collection)

collection.remove(7)#remove element
print(collection)

collection.clear()#empty the set
print(collection)
 
collection = {"hello", "python","php"}
collection.pop()#pick the random values
print(collection)

#two more important methods
set1 = {1,2,3,6,8,9}
set2 = {1,2,4,7,8,9}
print(set1.union(set2))#combines both set values & return new
print(set1.intersection(set2)) # combines common values & return new


# Practice questions
""" You are given a list of subjects for students.
 Assume one classroom is required for 1 subject.
How many classroom are needed by all students"""
# "python", "java", "php", "c++", c, "javascript",c++, "python", "java","python"
subjects = {"python", "java", "php", "c++", "c", "javascript","c++", "python", "java","python"}
print(len(subjects))

# Figure out a way to store 9 & 9.0 as separate values in the set
values = {9,9.0}#print only 9
values = {
    ("int",9),
    ("float",9.0)
}  
print(values)