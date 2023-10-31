class Student:
    count=0
    students=[]

    @classmethod
    def print(cls):
          print("------학생목록-------")
          print("이름\t총점\t")
          for student in cls.students:
               print(str(student))
          print("-----------------------")
          
    def __init__(self, name, korean, math, english, science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
        Student.count+=1
        Student.students.append(self)

    def get_sum(self):
         return self.korean+self.math+self.english+self.science
    
    def get_average(self):
         return self.get_sum()/4
    
    def __str__(self):
         return "{}\t{}\t{}".format(\
              self.name,\
              self.get_sum(),\
              self.get_average())
         
Student("윤인성1", 56, 90, 40, 60)
Student("윤인성2", 56, 90, 40, 60)
Student("윤인성3", 56, 90, 40, 60)
Student("윤인성4", 56, 90, 40, 60)
Student("윤인성5", 56, 90, 40, 60)
Student("윤인성6", 56, 90, 40, 60)
Student("윤인성7", 56, 90, 40, 60)

Student.print()