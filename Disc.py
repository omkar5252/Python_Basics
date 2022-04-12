x = 4000
discount=20

discount_amt=(x*discount)/100
print("discount_get=",discount_amt)

total_amt=x-discount_amt
print("Total_amt=",total_amt)


#Fibonacci series nth number
n=int(input("Enter the number:"))
if n<3:
    print(n-1)
else:
    a = 0
    b = 1
    for i in range(2,n):
        sum= a + b
        a = b
        b = sum
    print(sum,end=" ")
