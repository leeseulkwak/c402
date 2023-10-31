#딕셔너리를 리턴하는 함수를 선언한다

def create_student(name, korean, math, english, science):
    
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"]+student["math"]+student["english"]+student["science"]

def student_get_average(student):
    return student_get_sum(student)/4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))

students=[
    create_student("윤인성1", 50, 40, 50, 60),
    create_student("윤인성2", 50, 40, 50, 60),
    create_student("윤인성3", 50, 40, 50, 60),
    create_student("윤인성4", 50, 40, 50, 60),
    create_student("윤인성5", 50, 40, 50, 60),
    create_student("윤인성6", 50, 40, 50, 60)
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    print(student_to_string(student))