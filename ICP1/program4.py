score = int(input('enter score to check grade : ')) # enter integer value to get the grade
grade = " "
if score >= 94 and score <=100:         # if score is within 94 to 100 range then it prints grade A
    grade = 'A'
elif score >= 90 and score < 94:
    grade = 'A-'
elif score >= 87 and score < 90:
    grade = 'B+'
elif score >= 84 and score < 87:
    grade = 'B'
elif score >= 80 and score < 84:
    grade = 'B-'
elif score >= 77 and score < 80:
    grade = 'C+'
elif score >= 74 and score < 76:
    grade = 'C'
elif score >= 70 and score < 73:
    grade = 'C-'
elif score >= 67 and score < 69:
    grade = 'D+'
elif score >= 64 and score < 66:
    grade = 'D'
elif score >= 60 and score < 64:
    grade = 'D-'
elif score <= 60 and score >=0:
    grade = 'F'
else:                                   # if entered input is not within 0-100 then it displays out of range
    print("out of range")
print(grade)