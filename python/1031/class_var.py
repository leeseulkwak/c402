class Student:
    count=0

    def __init__(self, name, korean, math, english, science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

        Student.count+=1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

students=[
    Student("윤인성1", 87, 54, 54, 34),
    Student("윤인성2", 87, 54, 54, 34),
    Student("윤인성3", 87, 54, 54, 34)
        ]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))