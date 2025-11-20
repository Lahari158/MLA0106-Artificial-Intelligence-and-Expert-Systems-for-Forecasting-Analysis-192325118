import heapq

g = {
    'A': {'B': 2, 'C': 5},
    'B': {'D': 4, 'E': 1},
    'C': {'D': 2},
    'D': {'E': 3},
    'E': {}
}

def ucs(s, goal):
    pq = [(0, s, [])]
    vis = set()
    while pq:
        c, n, p = heapq.heappop(pq)
        if n in vis: continue
        vis.add(n)
        p = p + [n]
        if n == goal: return c, p
        for nb, w in g[n].items():
            heapq.heappush(pq, (c+w, nb, p))

def dijkstra(s, goal):
    pq = [(0, s)]
    dist = {x: 1e9 for x in g}
    dist[s] = 0
    while pq:
        c, n = heapq.heappop(pq)
        if n == goal: return c
        for nb, w in g[n].items():
            if c+w < dist[nb]:
                dist[nb] = c+w
                heapq.heappush(pq, (c+w, nb))

ucs_cost, path = ucs('A', 'E')
dij_cost = dijkstra('A', 'E')

print(path, ucs_cost, dij_cost)
