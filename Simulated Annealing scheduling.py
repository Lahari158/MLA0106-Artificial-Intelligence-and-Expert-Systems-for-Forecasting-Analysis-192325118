import random, math

tasks = range(6)
slots = [0,1,2]

def cost(s): return sum(max(0, s.count(x)-2) for x in slots)

def neigh(s):
    n = s[:]
    n[random.randint(0,5)] = random.choice(slots)
    return n

cur = [random.choice(slots) for _ in tasks]
best = cur[:]
T = 10

while T > 0.1:
    nx = neigh(cur)
    d = cost(nx) - cost(cur)
    if d < 0 or random.random() < math.exp(-d/T): cur = nx
    if cost(cur) < cost(best): best = cur[:]
    T *= 0.95

print("Best:", best, "Cost:", cost(best))
