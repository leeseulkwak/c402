def call_10_times(func):
    for i in range(10):
        func()

def hello():
    print("hi hello")

call_10_times(hello)