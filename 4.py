#Problem 4 : checked number is armstrong number or not

num=int(input("Enter a Number:"))
# here while loop is used to count digit of number 
digit = 0
temp = num
while(temp > 0):
   temp = temp // 10
   digit = digit + 1

# here for loop is used to checked number is greater than 0
sum = 0
temp = num
for i in range(1,temp+1):
    remainder = temp % 10
    temp = temp // 10
    sum = sum + remainder**digit

# here we used condition to checked number is armstrong or not
if (num == sum):
   print(num,"is armstrong number")
else:
   print(num,"is not Armstrong number")


