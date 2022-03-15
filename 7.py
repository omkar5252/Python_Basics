#Problem 7 : first 50 prime numbers

for i in range(1,51):
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        print(i,end=' ') 

