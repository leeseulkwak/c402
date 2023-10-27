#친구 찾기
py_graph = {
    'A': ['B'],
    'B': ['A','C','D'],
    'C': ['B','D','E'],
    'D': ['B','C','F'],
    'E': ['C','F','G'],
    'F': ['D','E','G'],
    'G': ['E','F']
}

data=input("누구의 친구를 찾으시나요\n")

if data == 'A':
    print(py_graph.get('A'))

elif data == 'B':
    print(py_graph.get('B'))

elif data == 'C':
    print(py_graph.get('C'))

elif data == 'D':
    print(py_graph.get('D'))

elif data == 'E':
    print(py_graph.get('E'))

elif data == 'F':
    print(py_graph.get('F'))

elif data == 'G':
    print(py_graph.get('G'))