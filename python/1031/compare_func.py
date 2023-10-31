class Student:
    def __init__(self, name, korean, math, english, science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

    def get_sum(self):
        return self.korean+self.math+self.english+self.science
        
    def get_avearage(self):
        return self.get_sum()/4
        
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avearage())
        
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
        
students=[
    Student("윤인성1", 50, 40, 50, 60),
    Student("윤인성2", 50, 40, 50, 60),
    Student("윤인성3", 50, 40, 50, 60),
    Student("윤인성4", 50, 40, 50, 60),
    Student("윤인성5", 50, 40, 50, 60)
]
    
student_a = Student("윤인성1", 50, 40, 50, 60 ),
student_b = Student("윤인성2", 50, 40, 50, 60 ),

print("student_a==student_b=", student_a==student_b)
print("student_a!=student_b=", student_a!=student_b)
print("student_a>student_b=", student_a>student_b)
print("student_a>=student_b=", student_a>=student_b)
print("student_a<student_b=", student_a<student_b)
print("student_a<=student_b=", student_a<=student_b)