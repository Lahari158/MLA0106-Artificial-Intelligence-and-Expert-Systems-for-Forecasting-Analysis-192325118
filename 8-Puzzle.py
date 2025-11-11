from queue import PriorityQueue  

def heuristic(state, goal):
    return sum(s != g for s, g in zip(state, goal))

def puzzle(start, goal):
    print("Initial State:", start)
    
    q = PriorityQueue()
    q.put((0, start))
    visited = set()

    while not q.empty():
        _, state = q.get()
        if state == goal:
            print("Goal Reached:", state)
            return
        visited.add(tuple(state))
        i = state.index(0)
        moves = []
        if i not in [0,1,2]: moves.append(i-3)
        if i not in [6,7,8]: moves.append(i+3)
        if i not in [0,3,6]: moves.append(i-1)
        if i not in [2,5,8]: moves.append(i+1)
        for m in moves:
            new = state[:]
            new[i], new[m] = new[m], new[i]
            if tuple(new) not in visited:
                q.put((heuristic(new, goal), new))

# Start and Goal states
start = [1,2,3,4,0,5,6,7,8]
goal  = [1,2,3,4,5,6,7,8,0]

puzzle(start, goal)
