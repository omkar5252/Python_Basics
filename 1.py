# calculate the percentage of student based on marks of any 5 subjects.

# Assume each subject is for 100 marks.
m = int(input("Enter marks of Maths:"))
s = int(input("Enter marks of Science:"))
h = int(input("Enter marks of History:"))
g = int(input("Enter marks of Geography:"))
s = int(input("Enter marks of sanskrit:"))

marks_obtain = m + s + h + g + s
total_marks = 500                        # each subject having 100 marks,so total marks=500.

p = marks_obtain/total_marks*100

print("Marks obtain:",marks_obtain)
print("Total marks:",total_marks)
print("Percentage of student is",p,"%.")
