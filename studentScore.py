class StudentProfile:
    def __init__(self,student_id,name,course,score):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.course=course
    def get_score(self):
        return self.score
    def update_score(self,new_score):
        if new_score>=0 and new_score<=100:
            self.score = new_score
            return 'True'
        else:
            return 'False'
    def get_status(self):
        if self.score>=60:
            return "Ready"
        else:
            return "Need Practice"
    def __str__(self):
        return (f"\nSTUDENT {i} PROFILE\nName: {stu.name}\nID: {stu.id}\nCourse: {stu.course}\nEmail: {stu.email}\nSkills: {stu.skills}")
studntPr
        

