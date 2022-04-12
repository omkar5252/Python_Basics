# take input from user
num_1=int(input("Enter the first number : "))
num_2=int(input("Enter the second number : "))

# select operation
print("1.addition :")
print("2.subtarction :")
print("3.multiplication :")
print("4.division :")
print("5.modulus :")
print("6.floor division :")
select = input("please select operation (1,2,3,4,5,6):")

# check operation and display result
# add two numbers
if select == "1":
    print("summation is :",num_1 + num_2)

# subtract two numbers
elif select == "2":
    print("subtraction is :",num_1 - num_2)

# multiply two numbers
elif select == "3":
    print("multiplication is :",num_1 * num_2)

# divison two numbers
elif select == "4":
    print("division is :",num_1 / num_2)

# modulus two numbers
elif select == "5":
    print("modulus is :",num_1 % num_2)

# floor division two numbers
elif select == "6":
    print("floor division is :",num_1 // num_2)

else:
    print("invalid input")







