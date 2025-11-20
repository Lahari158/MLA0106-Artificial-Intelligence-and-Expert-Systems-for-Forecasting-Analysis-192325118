# Minimax on perfect binary tree (root -> 2 internal nodes -> 4 leaves)

# Leaf values (game final states)
leaves = [3, 12, 8, 2]  # change as needed

def minimax(depth, index, isMax):
    if depth == 2:   # leaf level
        return leaves[index]
    left  = minimax(depth+1, index*2,     not isMax)
    right = minimax(depth+1, index*2 + 1, not isMax)
    return max(left, right) if isMax else min(left, right)

best_value = minimax(0, 0, True)

print("Best move value for maximizing player:", best_value)
