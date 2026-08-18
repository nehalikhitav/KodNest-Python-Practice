class StudentProfile:
    def __init__(self, name, id, course, email, skills):
        self.name = name
        self.id = id
        self.course = course
        self.email = email
        self.skills = skills
    def __str__(self):
        return (f"\nSTUDENT {i} PROFILE\nName: {stu.name}\nID: {stu.id}\nCourse: {stu.course}\nEmail: {stu.email}\nSkills: {stu.skills}")


students = []

n = int(input("Enter number of students: "))

for i in range(1,n+1):
    print(f"\nEnter details of Student{i}")
    name = input("Enter your name: ")
    id = input("Enter your ID: ")
    course = input("Enter your course: ")
    email = input("Enter your email: ")
    skills = list(map(str, input("Enter skills: ").split(',')))
    stu = StudentProfile(name, id, course, email, skills)
    students.append(stu)


print("\n===== STUDENT PROFILES =====")
i = 1
"""
instead of str method u can also print like this

for stu in students:
    print("\nSTUDENT", i, "PROFILE")
    print("Name:", stu.name)
    print("ID:", stu.id)
    print("Course:", stu.course)
    print("Email:", stu.email)
    print("Skills:", stu.skills)

    i+= 1"""