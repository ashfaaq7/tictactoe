import random

# Determine which player has to start the game first randomly
def first_player():
    return random.randint(1, 2)

# Get Player 1's marker choice at the start of the game => X or O
# Assign Player 2 the other marker
def player_choice():
    player1 = ''
    player2 = ''

    while player1.upper() not in ['X', 'O']:
        player1 = input("Player 1: Do you want to be X or O? ")
        print()
        if player1.upper() == 'X':
            player2 = 'O'
        elif player1.upper() == 'O':
            player2 = 'X'

    return (player1.upper(), player2.upper())

# Check if the players are ready and / wants to play again
def replay():
    play_again = ''

    while play_again.upper() not in ['YES', 'NO', 'Y', 'N']:
        play_again = input("Are you ready to play? Enter Yes or No. ")
        print()

    if  play_again.upper() in ['YES', 'Y']:
        return True
    elif play_again.upper() in ['NO', 'N']:
        return False

# Display the current board
def display_board(board):
    print("\n")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("   |   |   ")
    print("\n")

# Check if a position entered by the player is available
def position_check(position):
    if board[position] == " ":
        return True
    return False

# Check if there is a free space on the board for the player to choose
def board_space_check():
    for i in board:
        if i == " ":
            return True
    return False

# Get the player's preferred position to place X or O
def player_position(board, player):
    while True:
        position = input(f"Player {player} Choose your position (1 to 9): ")
        print()
        # If player enters a number string, continue. Else ask player to enter number again
        if position.isdigit():
            # Check if the position selected by the player is available, Else ask to choose another position
            if position_check(int(position)):
                #print("breaking pos check")
                break
            else:
                print("Position already played! Please enter a different position!")
                print()
        else:
            print("Please enter a digit from 1 to 9!")
            print()
    return int(position)

# Place the next marker on the board
def place_marker(board, marker, position):
    board[int(position)] = marker

# If space is available on the board, continue the game!
def game_on():
    return board_space_check()

# Check if any of the win condition is met
def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark or \
            board[4] == board[5] == board[6] == mark or \
                board[7] == board[8] == board[9] == mark or \
                    board[1] == board[5] == board[9] == mark or \
                        board[7] == board[5] == board[3] == mark or \
                            board[7] == board[4] == board[1] == mark or \
                                board[8] == board[5] == board[2] == mark or \
                                    board[9] == board[6] == board[3] == mark:
        return True
    return False

# Check if the board has only one space left
# If yes, return the index of the postion
def last_piece():
    num = 0
    idx = 0
    for i in board:
        if i == ' ':
            num += 1
            idx = board.index(i)
    if num == 1:
        return idx

    return None

# Game starts here!
# 1 2 3 4 5 6 7   => Positions for testing Win test case
# 1 2 3 4 7 5 6 9 => Positions for testing Tie test case
# 1 2 3 4 5 7 6 9 => Positions for testing Tie test case by auto populating last piece
# 1 9 7 3 6 8 5 2 => Positions for testing Win test case by auto populating last piece

while True:
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # Initialize players are ready first time
    ready = True
    winner = ''
    p1_marker = ''
    p2_marker = ''
    position = 0

    # If space available on the board, continue the game
    while game_on():
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print("Welcome to Tic Tac Toe!")
        print("Initial board!")
        display_board(board)
        marker_send = ''
        # Store the player's markers
        p1_marker, p2_marker = player_choice()
        # Determine which player has to start first
        player = first_player()
        # Flag for player
        player_1_flag = 1
        player_2_flag = 2

        # Assign the markers to the players based on player 1's choice
        if player == 1:
            print("Player", player, "will go first with marker <", p1_marker, ">")
            print()
            marker_send = p1_marker
        else:
            print("Player", player, "will go first with marker <", p2_marker, ">")
            print()
            marker_send = p2_marker

        # For first round, if players are ready to play, continue. Else set ready to false and end the game
        # If players want to play again, continue. Else end the game
        if replay():
            while board_space_check():
                # Check if only last piece of the board remains. If yes, last piece's index is stored in pos
                pos = last_piece()

                # If it is last piece, set the marker and check if there is any winner
                # If there is a winner, assign the current marker to winner
                if pos != None:
                    #print("last piece pos", pos, "marker", marker_send)
                    if marker_send == 'X':
                        place_marker(board, marker_send, pos)
                        print("\n"*100)
                        #print("display last piece if")
                        display_board(board)
                        if win_check(board, marker_send):
                            print("win_chk_pos:", marker_send)
                            winner = marker_send
                        break
                    elif marker_send == 'O':
                        place_marker(board, marker_send, pos)
                        print("\n"*100)
                        #print("display last piece else")
                        display_board(board)
                        if win_check(board, marker_send):
                            print("win_chk_pos:", marker_send)
                            winner = marker_send
                        break
                    else:
                        #print("pos break")
                        if win_check(board, marker_send):
                            print("win_chk_pos:", marker_send)
                            winner = marker_send
                        break

                # If it is not the last piece, get the player's preferred position and continue the game
                else:
                    position = player_position(board, player)

                    # Set the next player number alternatively as for the rest of the game
                    if player_1_flag == player:
                        player = player_2_flag
                    else:
                        player = player_1_flag

                    place_marker(board, marker_send, position)
                    print("\n"*100)
                    display_board(board)
                    if win_check(board, marker_send):
                        winner = marker_send
                        break

                    # Set the next marker alternatively as the players only need to select their position for
                    # the rest of the game
                    if marker_send == p1_marker:
                        marker_send = p2_marker
                    else:
                        marker_send = p1_marker

            # Check and announce the winner based on the last marker
            if winner == p1_marker:
                print("Congrats Player 1, YOU WIN!")
                print()
                break
            elif winner == p2_marker:
                print("Congrats Player 2, YOU WIN!")
                print()
                break
            else:
                #display_board(board)
                print("TIED!")
                print()
                break

        # If players are not ready for the first round, set ready to false
        else:
            ready = False
            break

    # End the game if players are not ready or don't want to play the game again!
    if not ready:
        break
    elif not replay():
        print("\n"*100)
        break