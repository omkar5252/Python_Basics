# Problem 3 : passenger and tkt price

n = int(input("Enter number of passengers:"))

tkt_price = 100
i=1
for i in range(1,n+1):
    print("\npassenger no:",i)

    age = int(input("Enter your age:"))
    if (age < 12):
        amt = tkt_price-(tkt_price*0.30)
        print("Passenger",i,"need to pay Rs.",amt)

    elif (age > 59):
        amt = tkt_price -(tkt_price*0.50)
        print("Passenger",i,"need to pay Rs.",amt)
        
    else:
        amt = tkt_price
        print("Passenger",i,"need to pay Rs.",amt)
    i+=1

       









