import itertools

d = {('A','B'):4,('A','C'):6,('A','D'):8,
     ('B','C'):3,('B','D'):7,('C','D'):5}

def dist(a,b): return d.get((a,b), d.get((b,a)))

cities = ['A','B','C','D']
start = 'A'
best = 1e9; bestp = None

for p in itertools.permutations([c for c in cities if c!=start]):
    path = [start,*p,start]
    cost = sum(dist(path[i],path[i+1]) for i in range(len(path)-1))
    if cost < best: best, bestp = cost, path

print("Route:", "->".join(bestp))
print("Cost:", best)
