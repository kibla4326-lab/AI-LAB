# 1. BFS without Queue & without Node

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs_without_queue(start):
    visited = [start]

    for node in visited:
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                
# 2. BFS with Queue & Node

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_with_queue(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        for child in node.children:
            queue.append(child)


# Create nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

A.children = [B, C]
B.children = [D, E]
C.children = [F]



print("BFS without Queue & Node:")
bfs_without_queue('A')

print("\n\nBFS with Queue & Node:")
bfs_with_queue(A)