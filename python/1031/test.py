# class Car:
#     def __init__(self, brand, model):
#         self._brand = brand     # 속성
#         self._model = model     # 속성

#     def drive(self):            # 메서드
#         print(f"Driving a {self._brand} {self._model}")

class MyClass: 
    class_var = "I'm a class variable"

    def __init__(self, value):
        self.instance_var = value

    def instance_method(self):
        return self.instance_var

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    def static_method():
        return "I'm a static method"

obj = MyClass("Instance value")
print(obj.instance_method())   # 출력: Instance value
print(MyClass.class_method())  # 출력: I'm a class variable
print(MyClass.static_method()) # 출력: I'm a static method
