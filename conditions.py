# number = int(input("pleas enter the number"))
# x = 5 

# if x > number:
#     print(x, "is gredeater then", number)
# else: 
#     print(x, "is lest then", number)    
    
name = input("Enter your name:")
age = input("Enter your age:")
age_limit = 21
if name == "Fatima" and int(age) >= age_limit:
    print("you are welcome to drink", name)
elif name == "Simon":
    print("you are banned", name)
else:
    print("your are too young")    
    
