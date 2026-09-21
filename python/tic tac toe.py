def player_choice():
    while True:
        choice = (input("Enter your choice(X,O): ")).upper()
        if choice == "X":
            return "X","O"
        elif choice == "O":
            return "O","X"
        else:
            print("Please enter either X or O")
player1, player2 = player_choice()

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("-----------")
    print(board[3], "|", board[4], "|", board[5])
    print("-----------")
    print(board[6], "|", board[7], "|", board[8])

def player1_marker(board):
    while True:
        try:
            player1_position = int(input("player1 Enter your position: "))
            if player1_position in range(1,10):
                if board[player1_position-1] == "X" or board[player1_position-1] == "O":
                    print("This position is taken")
                else:
                    return player1_position
            else:
                print("please enter a valid position")
        except ValueError:
            print("please enter a valid number")

def player2_marker(board):
    while True:
        try:
            player2_position = int(input("player2 Enter your position: "))
            if player2_position in range(1,10):
                if board[player2_position-1] == "X" or board[player2_position-1] == "O":
                    print("This position is taken")
                else:
                    return player2_position
            else:
                print("please enter a valid position")
        except ValueError:
            print("please enter a valid number")

winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def win_checker(board):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != " ":
            return 'win'
    if " " not in board:
            return 'tie'
    return 'continue'

def markers(board):
    while True:
        position1 = player1_marker(board)
        board[position1 - 1] = player1
        display_board(board)
        result = win_checker(board)
        if result == 'win':
            print("You won!")
            break
        elif result == 'tie':
            print("it's a tie!")
            break
        position2 = player2_marker(board)
        board[position2 - 1] = player2
        display_board(board)
        result = win_checker(board)
        if result == 'win':
            print("You won!")
            break
        elif result == 'tie':
            print("it's a tie!")
            break
markers(board)




