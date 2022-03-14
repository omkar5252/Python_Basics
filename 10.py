# Problem 10 :  calculate total salary of employee based on basic.

basic =float(input("Enter Basic salary:Rs."))
da = basic*0.10
ta = basic*0.12
hra = basic*0.15

total = basic + da + ta + hra
print("Total salary of employee is Rs.",total)