#lists in python
marks = [20, 70, 80, 30, 20, 50]
print("marks: " ,marks)

student = ["karan", 85, "kanpur"] #store different data types
print("name: ", student[0])
print("marks: ", student[1])
print("location: ", student[2])

student[1] = 90  # you can change index value bcz lists are mutable
print(student)

#list methods/functions
num_list = [1, 5 ,7 ,8,9, 5]
print(num_list.append(6)) # add value in last
print(num_list)

print(num_list.sort()) #sorts in Accending order
print(num_list)

print(num_list.sort(reverse = True)) #sorts in Decending order
print(num_list)

print(num_list.reverse()) #reverse list
print(num_list)

print(num_list.insert(2,4)) #insert element at index
print(num_list)

print(num_list.remove(5)) #remove 1st occurrence od element
print(num_list)

print(num_list.pop(3)) #remove index element
print(num_list)

#Practice question
# WAP to ask the user to enter names of their three favorite movies & store them in a list
# 1st way to solve it
movies = []
mov = input("enter 1st movie : ")
movies.append(mov)
mov = input("enter 2nd movie : ")
movies.append(mov)
mov = input("enter 3rd movie : ")
movies.append(mov)
print(movies)

# 2nd way to solve ques
movies = []
movies.append((input("enter your 1st movie : ")))
movies.append((input("enter your 2nd movie : ")))
movies.append((input("enter your 3rd movie : ")))
print(movies)

# WAP to check if a list contains palindrome of elements.
list1 = [1 , 3, 3 , 1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("NOT palindrome")

# WAP to store values in a list and sort them from "A" to "D"
list = ["C", "D", "A", "A", "B" ,"B","A"]
print(list.sort())
print(list)
    
