the_board = {
    "top_l": '', "top_m":'', "top_r": '',
    "mid_l": '', "mid_m": '', "mid_r": "",
    "low_l": '', "low_m":'', "low_r": ""
}

def printBoard(board):
    print(f"{board.get("top_l", '')} | {board.get("top_m", '')} | {board.get("top_r", '')}")
    print("-+-+-")
    print(f"{board.get("mid_l", '')} | {board.get("mid_m", '')} | {board.get("mid_r", '')}")
    print("-+-+-")
    print(f"{board.get("low_l", '')} | {board.get("low_m", '')} | {board.get("low_r", '')}")


turn = "X"
for i in range(9):
    printBoard(the_board)
    print(f"\nTurn {turn}. Move on wich space?")
    move = input()
    the_board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
