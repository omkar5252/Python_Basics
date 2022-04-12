#Fibonacci series

n=int(input("Enter the number:"))
a = 0
b = 1
print(a,b,end=" ")
for i in range(2,n):
    sum= a + b
    a = b
    b = sum
    print(sum,end=" ")

    

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

