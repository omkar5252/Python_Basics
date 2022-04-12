# taking input from user of ammount value and discount value
a = float(input("Enter ammount value:"))
b = float(input("Enter discount:"))
print()

#discount ammount value
discount_amt = (a * b)
print("Discount ammount:",discount_amt)

# final bill ammount value
final_bill= a - discount_amt
print("Final bill ammount:",final_bill)