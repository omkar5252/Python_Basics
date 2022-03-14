# Program 8 : calculate area of triangle and rectangle 

# Area of Traingle
a = int(input("Enter fisrt side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

# semi-perimeter of Triangle
s = (a + b + c)*0.5                        # formula of semi-perimeter 

# Area of Triangle
area = (s*(s-a)*(s-b)*(s-c))**0.5          # formula of Area of triangle
print("Area of traingle:",area)



# Area of Rectangle
l = int(input("Enter lenght:"))
b = int(input("Enter breadth:"))

a = l * b
print("Area of Rectangle:",a)