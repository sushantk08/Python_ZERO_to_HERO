student_data=[
    {
        "name":"Ram",
        "roll_no":10,
        "age":20,
        "course":"Python"
    },
    {
        "name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"Java"
    }
]

def add_new_entery(dict1):
    student_data.append(dict1)

dict1={
    "name":"Shyam",
    "roll_no":22,
    "age":18,
    "course":"C++"
}
new_entry=add_new_entery(dict1)
print(student_data)