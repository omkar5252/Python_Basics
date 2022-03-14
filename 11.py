# Problem 11 : the sum of three digit number

num = int(input("Enter 3 digit number:"))
sum = 0
sum = sum + (num % 10)

num = num//10
sum = sum + (num % 10)

num = num//10
sum += num % 10

print("sum of 3 digit number is",sum)