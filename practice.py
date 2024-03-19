lst=[
	    [101, 'John', 'IT', 60000],
	    [102, 'Alice', 'HR', 50000],
	    [103, 'Bob', 'Finance', 70000],
	    [104, 'Emma', 'IT', 55000],
	    [105, 'David', 'Finance', 75000],
	    [106, 'Sophia', 'HR', 48000]
]
department_info=[]

for employee_informaion in lst:
    _,_,department,salary=employee_informaion
    department_found=False
    for info in department_info:
        if info[0]==department:
            info[1] += salary
            info[2] += 1
            department_found=True
    if not department_found:
        department_info.append([department,salary,1])
for info in department_info:
    department,salary,no=info
    avg_salary=salary//no
    print(f"{department}-{avg_salary}")