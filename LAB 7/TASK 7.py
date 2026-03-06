# Artificial Intelligence - Lab 7
# A* Algorithm

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 2},
    'D': {},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def a_star(start, goal):
    open_list = [start]
    closed_list = []
    g = {start: 0}
    parent = {start: start}

    while open_list:
        n = None

        for v in open_list:
            if n is None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        if n == goal:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            print("Path found:", path)
            return

        open_list.remove(n)
        closed_list.append(n)

        for m in graph[n]:
            cost = graph[n][m]

            if m not in open_list and m not in closed_list:
                open_list.append(m)
                parent[m] = n
                g[m] = g[n] + cost

    print("Path does not exist")

a_star('A', 'G')
