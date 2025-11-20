N = 5  # smaller board gives quick output

moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
board = [[-1]*N for _ in range(N)]

def safe(x,y):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def tour(x,y,step):
    if step == N*N:
        return True
    for dx,dy in moves:
        nx,ny = x+dx, y+dy
        if safe(nx,ny):
            board[nx][ny] = step
            if tour(nx,ny,step+1):
                return True
            board[nx][ny] = -1
    return False

board[0][0] = 0
if tour(0,0,1):
    for r in board:
        print(r)
else:
    print("No solution")
