# Problem 7 : Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter a value in feets: "))
inch = float(input("Enter a value in inches: "))

f_m = feet * 0.304                 # here conversion feet = 0.304 meter
i_m = inch * 0.025                 # here conversion inch = 0.025 meter
total_m = f_m + i_m

f_cm = feet * 30.48                # here conversion feet = 30.48 centimeter
i_cm = feet * 2.54                 # here conversion inch = 2.54 centimeter
total_cm = f_cm + i_cm

print("Distant of feet and inches,converted in meter:",total_m)
print("Distant of feet and inches,converted in centimeter:",total_cm)



