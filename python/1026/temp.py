from queue import Queue

# 큐 생성
q = Queue()

# 요소 추가 (enqueue)
q.put(1)
q.put(2)
q.put(3)

# 요소 확인 (peek/front)
print(q.queue[0])  # 1

# 요소 제거 (dequeue)
print(q.get())  # 1

# 큐의 크기 확인
print(q.qsize())  # 2

# 큐가 비어있는지 확인
print(q.empty())  # False

# 남은 요소들 dequeue
print(q.get())  # 2
print(q.get())  # 3

# 큐가 비어있는지 확인
print(q.empty())  # True
