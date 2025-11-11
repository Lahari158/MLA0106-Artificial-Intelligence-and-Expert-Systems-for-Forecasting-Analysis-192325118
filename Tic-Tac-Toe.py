b = [' '] * 9

def show():
    print(f"{b[0]}|{b[1]}|{b[2]}")
    print("-+-+-")
    print(f"{b[3]}|{b[4]}|{b[5]}")
    print("-+-+-")
    print(f"{b[6]}|{b[7]}|{b[8]}")

def win(p):
    combos = [(0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6)]
    return any(b[x]==b[y]==b[z]==p for x,y,z in combos)

turn = 'X'
for i in range(9):
    show()
    move = int(input(f"Player {turn}, enter (0-8): "))
    if b[move] == ' ':
        b[move] = turn
        if win(turn):
            show()
            print(f"Player {turn} wins!")
            break
        turn = 'O' if turn == 'X' else 'X'
else:
    show()
    print("It's a draw!")
