#Dictionary in python
dict = {
    "name" : "Karan",
    "age"  :  22,
    "marks": ["88", "60" , "67"]
}
print(dict, type(dict))
#find data in dict
print("name:" ,dict["name"], "\n" "age:" ,dict["age"])

#assign new value
dict["age"] = 20
dict["marks"] = ["33", "45", "67"]
print(dict)

#add new key : value pair
dict["subject"] = ("math", "science", "art")
print(dict)

#create a null dict
null_dict = {}
print(type(null_dict))

#created nested dict
students = {
    "name" : "karan",
    "sub_marks" : {
        "phy" : 56,
        "chem": 98,
        "eng" : 78,
    },
    "status" : "pass"
}
print(students)
print(students["sub_marks"])
print(students["sub_marks"]["eng"])

#Dictionary methods
print(students.keys()) #returns key names
print(students.values()) # returns all values
print(students["sub_marks"].values())
print(students.items()) # returns all key : value pairs as tuple
print(students["sub_marks"].items())
print(students.get("status")) # returns the value according to key if key not present is gives -- None
new_dict = ({"qualification" : "graduated", "location" : "kanpur"})
students.update(new_dict) #add new key : value pairs
print(students)



# Practice questions....
# store some data in dict one key is store single value and second is store multiple values 
dict = {
    "cat" : "cats are sweet",
    "chairs" : ["tables are used to sit", "it is also used to keep something on that"]
}
print(dict)

# WAP to enter marks of 3 subjects from the user and store them in a dictinoary
marks = {}
x = (input("enter phy marks: "))
marks.update({"phy" : x})
x = (input("enter chem marks: "))
marks.update({"chem" : x})
x = (input("enter eng marks: "))
marks.update({"eng" : x})
print(marks)
