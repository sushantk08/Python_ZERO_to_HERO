students_marks={
    'jayesh':89,
    'suresh':91,
    'shubham':73,
    'ramesh':65,
    'paresh':57,
    'rakesh':43,
    'praksh': 38
}

students_grades={}

for student in students_marks:
    marks=students_marks[student]
    if marks>90:
        students_grades[student]="A+"
    elif marks>80 and marks<=90:
        students_grades[student]="A"
    elif marks>70 and marks<=80:
        students_grades[student]="B+"
    elif marks>60 and marks<=70:
        students_grades[student]="B"
    elif marks>50 and marks<=60:
        students_grades[student]="C"
    elif marks>40 and marks<=50:
        students_grades[student]="D"
    elif marks<=40:
        students_grades[student]="F"
    else:
        print("invalid marks")
print(students_grades)