marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "Computer": 95,
    "Physics": 88
}

total = sum(marks.values())
average = total / len(marks)
highest = max(marks.values())

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest Mark:", highest)
