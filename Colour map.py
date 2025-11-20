# Graph as adjacency list
graph = {
    'A': ['B','C'],
    'B': ['A','C','D'],
    'C': ['A','B','D'],
    'D': ['B','C']
}

colors = ['Red','Green','Blue']
solution = {}

def safe(node, color):
    for neigh in graph[node]:
        if neigh in solution and solution[neigh] == color:
            return False
    return True

def color_map(nodes):
    if not nodes:
        return True
    node = nodes[0]
    for c in colors:
        if safe(node, c):
            solution[node] = c
            if color_map(nodes[1:]): return True
            solution.pop(node)
    return False

nodes = list(graph.keys())
color_map(nodes)

print("Map Coloring Solution:")
for k in solution:
    print(k, "->", solution[k])
