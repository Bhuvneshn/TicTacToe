import random
ref_board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']*9


def show_ref_board():
    print("   |   |   ")
    print(" "+ref_board[0]+" | "+ref_board[1]+" | "+ref_board[2]+"  ")
    print("   |   |")
    print("---|---|---")
    print("   |   |")
    print(" "+ref_board[3]+" | "+ref_board[4]+" | "+ref_board[5]+"  ")
    print("   |   |")
    print("---|---|---")
    print("   |   |")
    print(" "+ref_board[6]+" | "+ref_board[7]+" | "+ref_board[8]+"  ")
    print("   |   |   ")


main_board = [" "]*9


def show_board():
    print("   |   |   ")
    print(" "+main_board[0]+" | "+main_board[1]+" | "+main_board[2]+"  ")
    print("   |   |")
    print("---|---|---")
    print("   |   |")
    print(" "+main_board[3]+" | "+main_board[4]+" | "+main_board[5]+"  ")
    print("   |   |")
    print("---|---|---")
    print("   |   |")
    print(" "+main_board[6]+" | "+main_board[7]+" | "+main_board[8]+"  ")
    print("   |   |   ")


winning_positions = [
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def menu():
    print('  ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋')
    print('❋                                       ❋')
    print('❋  1.REF - DISPLAYS THE REFERENCE BOARD ❋')
    print('❋                                       ❋')
    print('❋  2.BOARD - DISPLAYS THE CURRENT BOARD ❋')
    print('❋                                       ❋')
    print('❋  3.PLAY - PLAY A MOVE                 ❋')
    print('❋                                       ❋')
    print('  ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋')
    print()


diff = 'temp'
symbol = 'temp'


def initial():
    global diff
    while diff.lower().strip() not in ['impossible', 'easy', 'hard']:
        diff = input('   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n ❋                                               ❋ \n ❋ Choose difficulty level: EASY/HARD/IMPOSSIBLE ❋ \n ❋                                               ❋ \n   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n')
        diff = diff.lower().strip()
        print()
        print()
        if diff not in ['impossible', 'easy', 'hard']:
            print('PLEASE ENTER A VALID INPUT - ')

    global symbol
    while symbol.upper().strip() not in ['X', 'O']:
        symbol = input('   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n ❋                                               ❋ \n ❋           Choose your symbol: X / O           ❋ \n ❋                                               ❋ \n   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n')
        symbol = symbol.upper().strip()
        print()
        print()
        if symbol not in ['X', 'O']:
            print("ENTER A VALID INPUT - ")


def player_move():
    global symbol
    command = -1
    while command != 3:
        command = int(input("ENTER 1, 2 OR 3 - "))
        if command == 1:
            show_ref_board()
        elif command == 2:
            show_board()
        elif command == 3:
            print("REFERENCE BOARD :")
            show_ref_board()
            print()
            print()
            print("CURRENT BOARD :")
            show_board()
            print()
            move = -1
            while move not in possible_moves():
                move = int(
                    input("WHERE WOULD YOU LIKE TO PLACE YOUR "+symbol+" [0-8] - "))
                if move in possible_moves():
                    break
                else:
                    print("PLEASE ENTER AN EMPTY CELL NUMBER")
            main_board[move] = symbol
        else:
            print('INVALID INPUT. Please enter a valid input')


def possible_moves():
    moves = []
    for i in range(len(main_board)):
        if main_board[i] == ' ':
            moves.append(i)
    return moves


computer_symbol = None


def computer_move():
    global diff
    global computer_symbol
    computer_symbol = 'X' if symbol == 'O' else 'O'
    diff = diff.lower()
    moves = possible_moves()
    if diff == 'easy':
        comp_move = random.choice(moves)
        main_board[comp_move] = computer_symbol
    elif diff == 'hard':
        temp_board = main_board.copy()
        for i in moves:
            temp_board[i] = computer_symbol
            if check_win(computer_symbol, temp_board):
                main_board[i] = computer_symbol
                break
            else:
                temp_board[i] = ' '
        else:
            temp_board = main_board.copy()
            for i in moves:
                temp_board[i] = symbol
                if check_win(symbol, temp_board):
                    main_board[i] = computer_symbol
                    break
                else:
                    temp_board[i] = ' '
            else:
                comp_move = random.choice(moves)
                main_board[comp_move] = computer_symbol

    elif diff == 'impossible':
        temp_board = main_board.copy()
        for i in moves:
            temp_board[i] = computer_symbol
            if check_win(computer_symbol, temp_board):
                main_board[i] = computer_symbol
                break
            else:
                temp_board[i] = ' '
        else:
            temp_board = main_board.copy()
            for i in moves:
                temp_board[i] = symbol
                if check_win(symbol, temp_board):
                    main_board[i] = computer_symbol
                    break
                else:
                    temp_board[i] = ' '
            else:
                corners = [0, 2, 6, 8]
                corners_available = []
                for o in corners:
                    if o in moves:
                        corners_available.append(o)
                if len(corners_available) > 1:
                    comp_move = random.choice(corners_available)
                    main_board[comp_move] = computer_symbol
                elif 4 in moves:
                    main_board[4] = computer_symbol
                else:
                    side_available = []
                    sides = [1, 3, 5, 7]
                    for side in sides:
                        if side in moves:
                            side_available.append(side)
                    comp_move = random.choice(side_available)
                    main_board[comp_move] = computer_symbol


def check_win(sym, board):
    for i in winning_positions:
        if board[i[0]] == board[i[1]] == board[i[2]] == sym:
            return 1
    return 0


def check_draw(board):
    for i in winning_positions:
        if board[i[0]] == board[i[1]] == board[i[2]] == computer_symbol:
            return 0
        if board[i[0]] == board[i[1]] == board[i[2]] == symbol:
            return 0
    if ' ' not in board:
        return 1


x = 1


def end():
    inp2 = int(input("1. PLAY AGAIN \n2. EXIT \n"))
    if inp2 == 1:
        global main_board
        global diff
        global symbol
        symbol = 'temp'
        diff = 'temp'
        main_board = [" "]*9
        initial()
        game()
    elif inp2 == 2:
        print('THANK YOU FOR PLAYING!')
        global x
        x = 0


def game():
    initial()
    global diff
    global symbol
    menu()
    if symbol == 'X':
        player_move()
        if check_draw(main_board):
            show_board()
            print("IT'S A DRAW! WELL PLAYED!")
            print()
            end()
        if check_win(symbol, main_board):
            show_board()
            print('WELL PLAYED! YOU WON!')
            print()
            end()
        else:
            computer_move()
            print("COMPUTER'S MOVE - ")
            show_board()
            if check_draw(main_board):
                print("IT'S A DRAW! WELL PLAYED!")
                print()
                end()
            if check_win(computer_symbol, main_board):
                print('YOU LOST! FEEL FREE TO PLAY AGAIN')
                print()
                end()
    else:
        computer_move()
        print("COMPUTER'S MOVE - ")
        show_board()
        if check_draw(main_board):
            print("IT'S A DRAW! WELL PLAYED!")
            print()
            end()
        if check_win(computer_symbol, main_board):
            print('YOU LOST! FEEL FREE TO PLAY AGAIN')
            print()
            end()

        else:
            player_move()
            if check_draw(main_board):
                show_board()
                print("IT'S A DRAW! WELL PLAYED!")
                print()
                end()
            if check_win(symbol, main_board):
                show_board()
                print('WELL PLAYED! YOU WON!')
                print()
                end()


while x == 1:
    game()
