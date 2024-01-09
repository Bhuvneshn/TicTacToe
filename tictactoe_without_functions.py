import random
ref_board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

main_board = [" "]*9

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

diff = 'temp'
symbol = 'temp'
computer_symbol = None

x = 1

while x == 1:
    while diff.lower().strip() not in ['impossible', 'easy', 'hard']:
        diff = input('   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n ❋                                               ❋ \n ❋ Choose difficulty level: EASY/HARD/IMPOSSIBLE ❋ \n ❋                                               ❋ \n   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n')
        diff = diff.lower().strip()
        print()
        print()
        if diff not in ['impossible', 'easy', 'hard']:
            print('PLEASE ENTER A VALID INPUT - ')

    while symbol.upper().strip() not in ['X', 'O']:
        symbol = input('   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n ❋                                               ❋ \n ❋           Choose your symbol: X / O           ❋ \n ❋                                               ❋ \n   ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ ❋ \n')
        symbol = symbol.upper().strip()
        print()
        print()
        if symbol not in ['X', 'O']:
            print("ENTER A VALID INPUT - ")

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

    if symbol == 'X':
        command = -1
        while command != 3:
            command = int(input("ENTER 1, 2 OR 3 - "))
            if command == 1:
                print("   |   |   ")
                print(" "+ref_board[0]+" | " +
                      ref_board[1]+" | "+ref_board[2]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+ref_board[3]+" | " +
                      ref_board[4]+" | "+ref_board[5]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+ref_board[6]+" | " +
                      ref_board[7]+" | "+ref_board[8]+"  ")
                print("   |   |   ")
            elif command == 2:
                print("   |   |   ")
                print(" "+main_board[0]+" | " +
                      main_board[1]+" | "+main_board[2]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[3]+" | " +
                      main_board[4]+" | "+main_board[5]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[6]+" | " +
                      main_board[7]+" | "+main_board[8]+"  ")
                print("   |   |   ")
            elif command == 3:
                print("REFERENCE BOARD :")
                print("   |   |   ")
                print(" "+ref_board[0]+" | " +
                      ref_board[1]+" | "+ref_board[2]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+ref_board[3]+" | " +
                      ref_board[4]+" | "+ref_board[5]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+ref_board[6]+" | " +
                      ref_board[7]+" | "+ref_board[8]+"  ")
                print("   |   |   ")
                print()
                print()
                print("CURRENT BOARD :")
                print("   |   |   ")
                print(" "+main_board[0]+" | " +
                      main_board[1]+" | "+main_board[2]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[3]+" | " +
                      main_board[4]+" | "+main_board[5]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[6]+" | " +
                      main_board[7]+" | "+main_board[8]+"  ")
                print("   |   |   ")
                print()
                move = -1
                possible_moves = []
                for i in range(len(main_board)):
                    if main_board[i] == ' ':
                        possible_moves.append(i)
                while move not in possible_moves:
                    move = int(
                        input("WHERE WOULD YOU LIKE TO PLACE YOUR "+symbol+" [0-8] - "))
                    if move in possible_moves:
                        break
                    else:
                        print("PLEASE ENTER AN EMPTY CELL NUMBER")
                main_board[move] = symbol
            else:
                print('INVALID INPUT. Please enter a valid input')

        for i in winning_positions:
            if (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == computer_symbol) or (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == symbol):
                some_win = True
                break
            else:
                some_win = False
        if (' ' not in main_board) and not(some_win):
            is_draw = True
        else:
            is_draw = False
        if is_draw:
            print("   |   |   ")
            print(" "+main_board[0]+" | " +
                  main_board[1]+" | "+main_board[2]+"  ")
            print("   |   |")
            print("---|---|---")
            print("   |   |")
            print(" "+main_board[3]+" | " +
                  main_board[4]+" | "+main_board[5]+"  ")
            print("   |   |")
            print("---|---|---")
            print("   |   |")
            print(" "+main_board[6]+" | " +
                  main_board[7]+" | "+main_board[8]+"  ")
            print("   |   |   ")
            print("IT'S A DRAW! WELL PLAYED!")
            print()
            print("THANK YOU FOR PLAYING!")
            break

        for i in winning_positions:
            if main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == symbol:
                is_win = True
                break
            else:
                is_win = False

        if is_win:
            print("   |   |   ")
            print(" "+main_board[0]+" | " +
                  main_board[1]+" | "+main_board[2]+"  ")
            print("   |   |")
            print("---|---|---")
            print("   |   |")
            print(" "+main_board[3]+" | " +
                  main_board[4]+" | "+main_board[5]+"  ")
            print("   |   |")
            print("---|---|---")
            print("   |   |")
            print(" "+main_board[6]+" | " +
                  main_board[7]+" | "+main_board[8]+"  ")
            print("   |   |   ")
            print('WELL PLAYED! YOU WON!')
            print()
            print("THANK YOU FOR PLAYING!")
            break
        else:
            computer_symbol = 'X' if symbol == 'O' else 'O'
            diff = diff.lower()
            moves = []
            for i in range(len(main_board)):
                if main_board[i] == ' ':
                    moves.append(i)
            if diff == 'easy':
                comp_move = random.choice(moves)
                main_board[comp_move] = computer_symbol
            elif diff == 'hard':
                temp_board = main_board.copy()
                for i in moves:
                    temp_board[i] = computer_symbol
                    for j in winning_positions:
                        if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == computer_symbol:
                            is_win_fake = True
                            break
                        else:
                            is_win_fake = False
                    if is_win_fake:
                        main_board[i] = computer_symbol
                        break
                    else:
                        temp_board[i] = ' '
                else:
                    temp_board = main_board.copy()
                    for i in moves:
                        temp_board[i] = symbol
                        for j in winning_positions:
                            if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == symbol:
                                is_win_fake = True
                                break
                            else:
                                is_win_fake = False
                        if is_win_fake:
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
                    for j in winning_positions:
                        if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == computer_symbol:
                            is_win_fake = True
                            break
                        else:
                            is_win_fake = False
                    if is_win_fake:
                        main_board[i] = computer_symbol
                        break
                    else:
                        temp_board[i] = ' '
                else:
                    temp_board = main_board.copy()
                    for i in moves:
                        temp_board[i] = symbol
                        for j in winning_positions:
                            if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == symbol:
                                is_win_fake = True
                                break
                            else:
                                is_win_fake = False
                        if is_win_fake:
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
            print("COMPUTER'S MOVE - ")
            print("   |   |   ")
            print(" "+main_board[0]+" | " +
                  main_board[1]+" | "+main_board[2]+"  ")
            print("   |   |")
            print("---|---|---")
            print("   |   |")
            print(" "+main_board[3]+" | " +
                  main_board[4]+" | "+main_board[5]+"  ")
            print("   |   |")
            print("---|---|---")
            print("   |   |")
            print(" "+main_board[6]+" | " +
                  main_board[7]+" | "+main_board[8]+"  ")
            print("   |   |   ")
            for i in winning_positions:
                if (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == computer_symbol) or (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == symbol):
                    some_win_2 = True
                    break
                else:
                    some_win_2 = False
            if (' ' not in main_board) and not(some_win_2):
                is_draw_2 = True
            else:
                is_draw_2 = False

            if is_draw_2:
                print("IT'S A DRAW! WELL PLAYED!")
                print()
                print("THANK YOU FOR PLAYING")
                break

            for i in winning_positions:
                if main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == computer_symbol:
                    is_win_2 = True
                    break
                else:
                    is_win_2 = False
            if is_win_2:
                print('YOU LOST! FEEL FREE TO PLAY AGAIN')
                print()
                break

    else:
        computer_symbol = 'X' if symbol == 'O' else 'O'
        diff = diff.lower()
        moves = []
        for i in range(len(main_board)):
            if main_board[i] == ' ':
                moves.append(i)
        if diff == 'easy':
            comp_move = random.choice(moves)
            main_board[comp_move] = computer_symbol
        elif diff == 'hard':
            temp_board = main_board.copy()
            for i in moves:
                temp_board[i] = computer_symbol
                for j in winning_positions:
                    if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == computer_symbol:
                        is_win_fake = True
                        break
                    else:
                        is_win_fake = False
                if is_win_fake:
                    main_board[i] = computer_symbol
                    break
                else:
                    temp_board[i] = ' '
            else:
                temp_board = main_board.copy()
                for i in moves:
                    temp_board[i] = symbol
                    for j in winning_positions:
                        if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == symbol:
                            is_win_fake = True
                            break
                        else:
                            is_win_fake = False
                    if is_win_fake:
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
                for j in winning_positions:
                    if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == computer_symbol:
                        is_win_fake = True
                        break
                    else:
                        is_win_fake = False
                if is_win_fake:
                    main_board[i] = computer_symbol
                    break
                else:
                    temp_board[i] = ' '
            else:
                temp_board = main_board.copy()
                for i in moves:
                    temp_board[i] = symbol
                    for j in winning_positions:
                        if temp_board[j[0]] == temp_board[j[1]] == temp_board[j[2]] == symbol:
                            is_win_fake = True
                            break
                        else:
                            is_win_fake = False
                    if is_win_fake:
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
        print("COMPUTER'S MOVE - ")
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

        for i in winning_positions:
            if (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == computer_symbol) or (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == symbol):
                some_win_3 = True
                break
            else:
                some_win_3 = False
        if (' ' not in main_board) and not(some_win_3):
            is_draw_3 = True
        else:
            is_draw_3 = False

        if is_draw_3:
            print("IT'S A DRAW! WELL PLAYED!")
            print()
            break
        for i in winning_positions:
            if main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == computer_symbol:
                is_win_3 = True
                break
            else:
                is_win_3 = False

        if is_win_3:
            print('YOU LOST! FEEL FREE TO PLAY AGAIN')
            print()
            break
        if not(is_draw_3) and not(is_win_3):
            command = -1
            while command != 3:
                command = int(input("ENTER 1, 2 OR 3 - "))
                if command == 1:
                    print("   |   |   ")
                    print(" "+ref_board[0]+" | " +
                          ref_board[1]+" | "+ref_board[2]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+ref_board[3]+" | " +
                          ref_board[4]+" | "+ref_board[5]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+ref_board[6]+" | " +
                          ref_board[7]+" | "+ref_board[8]+"  ")
                    print("   |   |   ")
                elif command == 2:
                    print("   |   |   ")
                    print(" "+main_board[0]+" | " +
                          main_board[1]+" | "+main_board[2]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+main_board[3]+" | " +
                          main_board[4]+" | "+main_board[5]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+main_board[6]+" | " +
                          main_board[7]+" | "+main_board[8]+"  ")
                    print("   |   |   ")
                elif command == 3:
                    print("REFERENCE BOARD :")
                    print("   |   |   ")
                    print(" "+ref_board[0]+" | " +
                          ref_board[1]+" | "+ref_board[2]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+ref_board[3]+" | " +
                          ref_board[4]+" | "+ref_board[5]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+ref_board[6]+" | " +
                          ref_board[7]+" | "+ref_board[8]+"  ")
                    print("   |   |   ")
                    print()
                    print()
                    print("CURRENT BOARD :")
                    print("   |   |   ")
                    print(" "+main_board[0]+" | " +
                          main_board[1]+" | "+main_board[2]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+main_board[3]+" | " +
                          main_board[4]+" | "+main_board[5]+"  ")
                    print("   |   |")
                    print("---|---|---")
                    print("   |   |")
                    print(" "+main_board[6]+" | " +
                          main_board[7]+" | "+main_board[8]+"  ")
                    print("   |   |   ")
                    print()
                    move = -1
                    possible_moves_2 = []
                    for i in range(len(main_board)):
                        if main_board[i] == ' ':
                            possible_moves_2.append(i)
                    while move not in possible_moves_2:
                        move = int(
                            input("WHERE WOULD YOU LIKE TO PLACE YOUR "+symbol+" [0-8] - "))
                        if move in possible_moves_2:
                            break
                        else:
                            print("PLEASE ENTER AN EMPTY CELL NUMBER")
                    main_board[move] = symbol
                else:
                    print('INVALID INPUT. Please enter a valid input')

            for i in winning_positions:
                if (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == computer_symbol) or (main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == symbol):
                    some_win_4 = True
                    break
                else:
                    some_win_4 = False
            if (' ' not in main_board) and not(some_win_4):
                is_draw_4 = True
            else:
                is_draw_4 = False

            if is_draw_4:
                print("   |   |   ")
                print(" "+main_board[0]+" | " +
                      main_board[1]+" | "+main_board[2]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[3]+" | " +
                      main_board[4]+" | "+main_board[5]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[6]+" | " +
                      main_board[7]+" | "+main_board[8]+"  ")
                print("   |   |   ")
                print("IT'S A DRAW! WELL PLAYED!")
                print()
                break

            for i in winning_positions:
                if main_board[i[0]] == main_board[i[1]] == main_board[i[2]] == symbol:
                    is_win_4 = True
                    break
                else:
                    is_win_4 = False
            if is_win_4:
                print("   |   |   ")
                print(" "+main_board[0]+" | " +
                      main_board[1]+" | "+main_board[2]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[3]+" | " +
                      main_board[4]+" | "+main_board[5]+"  ")
                print("   |   |")
                print("---|---|---")
                print("   |   |")
                print(" "+main_board[6]+" | " +
                      main_board[7]+" | "+main_board[8]+"  ")
                print("   |   |   ")
                print('WELL PLAYED! YOU WON!')
                print()
                break
