from collections import deque

def water_jug(j1, j2, target):
    q = deque([(0, 0)])
    visited = set()

    while q:
        a, b = q.popleft()
        if a == target or b == target:
            print(f"Reached Target: ({a}, {b})")
            return
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(f"State: ({a}, {b})")
        q.extend([
            (j1, b), (a, j2), (0, b), (a, 0),
            (a - min(a, j2 - b), b + min(a, j2 - b)),
            (a + min(b, j1 - a), b - min(b, j1 - a))
        ])

water_jug(4, 3, 2)
