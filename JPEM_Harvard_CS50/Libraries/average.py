import statistics as stat

avg_grade = stat.mean([100,90, 78, 50, 98, 67])

print(avg_grade)

if avg_grade >= 90:
    print("Your average grade is A")
elif avg_grade >= 80:
    print("Your average grade is B")
elif avg_grade >= 70:
    print("Your average grade is C")
elif avg_grade >= 60:
    print("Your average grade is D")
else:
    print("Your average grade is an F")