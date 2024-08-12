def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j in {3,6}:
                print(" |", end = "") 
            print(f" {board[i][j]}",end = "")
        print("")
        if i in {2,5}:
            for j in range(len(board[0])):
                if j in {3,6}:
                    print(" |", end = "") 
                print(" -",end = "")
            print("")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return (-1,-1)

def valid(board,num,pos):
    row,col = pos[0],pos[1]
    # check horizontal
    for j in range(len(board[0])):
        if board[row][j] == num and col != j:
            return False

    # check vertical
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False
    
    # check 3*3 grid
    subrow = row//3
    subcol = col//3
    for i in range(subrow * 3, (subrow * 3) + 3):
        for j in range(subcol * 3, (subcol * 3) + 3):
            if board[i][j] == num and pos != (i,j):
                return False
            # board[i][j] = "X" #dbg

    return True

def solve(board):
    find = find_empty(board)
    if find == (-1,-1):
        return True
    else:
        row, col = find

    for n in range(1,10):
        if valid(board,n,(row,col)):
            board[row][col] = n

            if solve(board):
                return True
            board[row][col] = 0

    return False
    
if __name__ == "__main__":
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    print_board(board)
    solve(board)
    print("___________________\n")
    print_board(board)