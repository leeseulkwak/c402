
def bfs(graph, start, max_depth):

    #방문한 노드를 저장할 집합

    visited = set()
    #탐색할 노드와 현재 깊이(촌수)를 저장하는 큐

    queue=[(start, 0)]

    #관련된 사람들과 그들과의 촌수를 저장할 리스트
    related_people=[]

    while queue: #큐에 탐색할 노드가 남아 있다면 반복
        person, depth=queue.pop(0) #큐의 첫번째 노드와 그노의 깊이 (촌수)를 가져옴

    if depth<=max_depth and person!=start:
            related_people.append((person, depth))

    if person not in visited:
            visited.add(person)

    for neighbor in graph.get(person, []):
        if neighbor not in visited:
                    queue.append((neighbor, depth+1))

        return related_people
    
def main():
    print("가능한 사람들:", ",".join(py_graph.keys()))

    person=input("자신의 이름을 입력하세요")

    if person not in py_graph:
        print(f"{person}은/는 그래프에 없습니다.")
        return
        
    depth=int(input(f"몇 촌 이내의 친척을 찬고 싶은지 입력하세요(예:1촌, 2촌 등):"))
    related_people=bfs(py_graph, person, depth)

    print(f"{person}의 {depth}촌 이내 친척들:")
    for p, d in related_people:
            print(f"{p}({d}촌)")


py_graph = {
    'A': ['B'],
    'B': ['A','C','D'],
    'C': ['B','D','E'],
    'D': ['B','C','F'],
    'E': ['C','F','G'],
    'F': ['D','E','G'],
    'G': ['E','F']
}
    

#프로그램 시작

if __name__ == "__main__":
    main()
