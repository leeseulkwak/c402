#딕셔너리를 리턴하는 함수를 선언한다

def create_student(name, korean, math, english, science):
    
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

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
    score_sum=student["korean"]+student["math"]+student["english"]+student["science"]
    average=score_sum/4

    print(student["name"], score_sum, average, sep="\t")