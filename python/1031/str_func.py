class Student:
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
        
    students=[
        Student("윤인성1", 50, 40, 50, 60),
        Student("윤인성2", 50, 40, 50, 60),
        Student("윤인성3", 50, 40, 50, 60),
        Student("윤인성4", 50, 40, 50, 60),
        Student("윤인성5", 50, 40, 50, 60),
]
    
    print("이름", "총점", "평균", sep="\t")
    for student in students:
        print(str(student))