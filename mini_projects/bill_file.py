# file handling in python
userName = input("Enter your name: ")
number = input("Enter your number: ")
unit = int(input("Enter unit: "))
amount = unit*5
fix_char= 150
payable_amnt = amount + fix_char
net_payable = payable_amnt

f = open(f"files/{userName}.txt","a")
f.write("============billing software=================\n")
f.write(f"Name: {userName}\n")
f.write(f"Number: {number}\n")
f.write(f"Unit: {unit}\n")
f.write("=============================================\n")
f.write(f"Amount: {amount}\n")
f.write(f"Fix Charges: {fix_char}\n")
f.write(f"Payable Amount: {payable_amnt}\n")
f.write("=============================================\n")
f.write(f"Net Paybale:{net_payable}\n")







