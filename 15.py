# Problem 15: program to accept an integer amount from user 
# and tell minimum number of notes needed 
#for representing that amount.

num = int(input("Enter ammount:Rs."))

sum =0
sum1 = sum + (num//1000)        
num = num % 1000

sum2 = sum + (num//500)
num = num % 500

sum3 = sum + (num//100)
num = num % 100

sum4 = sum + (num//50)
num = num % 50

sum5 = sum + (num//20)
num = num % 20

sum6 = sum + (num//10)
sum += num % 10

print("Notes of Rs.1000:",sum1)
print("Notes of Rs.500:",sum2)
print("Notes of Rs.100:",sum3)
print("Notes of Rs.50:",sum4)
print("Notes of Rs.20:",sum5)
print("Notes of Rs.10:",sum6)

total = sum1 + sum2 + sum3 + sum4 + sum5 + sum6
print("Minimum number of note required:",total)