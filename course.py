class course:
    def __init__(self,name,duration,trainer_name,technologies,start_date):
        self.name=name
        self.duaration=duration
        self.trainer_name=trainer_name
        self.technologies=technologies
        self.start_date=start_date
    def display(self):
        print("Course Details:")
        print("Name:",self.name)
        print("Duration:",self.duaration)
        print("Trainer Name:",self.trainer_name)
        print("Technologies:",self.technologies)
        print("Start Date:",self.start_date) 

name=input().strip()
duration=input().strip()
trainer_name=input().strip()
tech=list(map(str,input().strip().split()))
start_date=input().strip()
course1=course(name,duration,trainer_name,tech,start_date)
course1.display()