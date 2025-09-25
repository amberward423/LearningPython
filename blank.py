

def add_student(students, name, subject):
    return students, name, subject

def update_grade(students, name, subject,new_score):
    return students, name, subject, new_score

def add_subject(students, name, new_subject, score):
    return students, name, new_subject, score

def print_subject(students,name):
    return students, name

def get_average(students,name):
    return students, name

students ={
    "Janice": {"Math": 88, "English": 100},
    "Edward": {"Math": 93, "English": 73 }
}
name = "Janice", "Edward", "Charlie"
subject= "Math", "Art", "English"
score= 93, 73,88, 100, 60, 99
# What I had """
#students["Janice"]= {"Math": 88, "English": 100}
# students["Edward"]= {"Math":93, "English": 73}
#print(f"{students["Janice"]} your score for Math is: " , {students["Janice"]})

#what the teacher had

print("Janice's math score: ", students["Janice"]["Math"])

print("Edwards english score: ", students["Edward"]["English"])

students["Edward"]["Art"] = 50

students["Janice"]["Math"]= 89

students["Charlie"]= {"Math": 60, "English": 99}

del students ["Edward"]["Math"]

print("The whole students dictionary: ")

for s in students:
    print(s, students[s])




