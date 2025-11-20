import heapq

g = {
 'A':{'B':1,'C':4},
 'B':{'D':3,'E':5},
 'C':{'F':2},
 'D':{'F':1,'E':1},
 'E':{'F':2},
 'F':{}
}

h = {'A':6,'B':4,'C':2,'D':1,'E':2,'F':0}

def astar(s, t):
    pq=[(h[s],0,s,[s])]
    vis=set()
    print("Expand:")
    while pq:
        f,gc,u,p = heapq.heappop(pq)
        if u in vis: continue
        vis.add(u); print(u,end=" ")
        if u==t:
            print("\nPath:", "->".join(p))
            print("Cost:", gc); return
        for v,w in g[u].items():
            if v not in vis:
                ng = gc+w
                heapq.heappush(pq,(ng+h[v],ng,v,p+[v]))

astar('A','F')
