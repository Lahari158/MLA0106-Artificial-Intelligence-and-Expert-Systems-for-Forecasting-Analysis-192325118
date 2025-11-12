rules = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

facts = {'D'}

def backward_chaining(goal):
    if goal in facts:
        return True
    if goal not in rules:
        return False
    return all(backward_chaining(subgoal) for subgoal in rules[goal])

goal = 'A'
print("Can we prove", goal, "?", backward_chaining(goal))



