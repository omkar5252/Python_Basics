# Problem 5 : Convert the time entered in hh,min and sec into seconds

hh = int(input("Enter number of hours: "))
min = int(input("Enter number of minutes: "))
sec = int(input("Enter number of seconds: "))

hh_sec = hh*3600          # 1Hr = 3600 sec
min_sec = min*60          # 1Min = 60 sec
sec = sec                

total = hh_sec + min_sec + sec

print("Hour convert into seconds:",hh_sec,"sec.")
print("Minute convert into seconds:",min_sec,"sec.")
print("Second convert into seconds:",sec,"sec.")
print("Total time convert into seconds:",total,"sec.")