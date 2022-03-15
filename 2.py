#Problem 2 : percentage of students

n = int(input("Enter number of students:"))
for i in range(1,n+1) :
    print("student no:",i)
    m = int(input("\nEnter marks of Marathi:"))
    h = int(input("Enter marks of History:"))
    s = int(input("Enter marks of Science:"))
    p = int(input("Enter marks of Physics:"))
    g = int(input("Enter marks of Geography:"))

    marks_obtain = m + h + s + p + g
    total_marks = 500

    percentage = (marks_obtain/total_marks)*100
    print("\nPercentage:",percentage)
    i+=1
    
