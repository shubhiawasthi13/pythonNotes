# Project-1 Guess the target
import random
target = random.randint(1,10)


while True:
    UserChoice = input("Guess the target or Quit : ")
    if(UserChoice == "Quit"):
        break

    UserChoice = int(UserChoice)
    if(UserChoice == target):
        print("Success : Correct Guess")
        break
    elif(UserChoice < target):
        print("Your number was too small. Take a bigger number")
    else:
        print("Your number was too big. Take a smaller number")

print("-------Game Over--------")        



# Project-2 Random password genrator
import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password+=random.choice(charValues)

# # list comperhension.....short hand
# password = "".join([random.choice(charValues) for i in range(pass_len)]) 


print("Random password: ", password)
