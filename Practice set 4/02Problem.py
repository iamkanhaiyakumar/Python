# Write a program to accept marks of 6 marks and display them in a sorted.

# Solution: 
marks = []

f1 = int(input ("Enter Marks Here : "))
marks.append(f1)
f2 = int(input ("Enter Marks Here : "))
marks.append(f2)
f3 = int(input ("Enter Marks Here : "))
marks.append(f3)
f4 = int(input ("Enter Marks Here : "))
marks.append(f4)
f5 = int(input ("Enter Marks Here : "))
marks.append(f5)
f6 = int(input ("Enter Marks Here : "))
marks.append(f6)
f7 = int(input ("Enter Marks Here : "))
marks.append(f7)

marks.sort()
print(marks)