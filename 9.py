# Problem 9 :  calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter cost price of book:Rs."))
discount = float(input("Enter discount :"))

discount_price = (cost_price * discount)
selling_price = cost_price - discount_price

print("Discount price:Rs",discount_price)
print("selling price of book :Rs.",selling_price)
