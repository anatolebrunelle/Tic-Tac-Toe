import random
import time
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

def place_to_int(y, x):
    return y * 3 + x + 1


def int_to_place(x, board):
    row = (x - 1) // 3
    col = (x - 1) % 3
    return board[row][col]



def move(x, board, player):
    if x > 9 or x < 0:
        print("Veuillez choisir un nombre valide")
    else :
        place = int_to_place(x, board)
        if place == " ":
            match player:
                case 1:
                    match x:
                        case 1:
                            board[0][0] = "X"
                        case 2:
                            board[0][1] = "X"
                        case 3:
                            board[0][2] = "X"
                        case 4:
                            board[1][0] = "X"
                        case 5:
                            board[1][1] = "X"
                        case 6:
                            board[1][2] = "X"
                        case 7:
                            board[2][0] = "X"
                        case 8:
                            board[2][1] = "X"
                        case 9:
                            board[2][2] = "X"
                case 2:
                    match x:
                        case 1:
                            board[0][0] = "O"
                        case 2:
                            board[0][1] = "O"
                        case 3:
                            board[0][2] = "O"
                        case 4:
                            board[1][0] = "O"
                        case 5:
                            board[1][1] = "O"
                        case 6:
                            board[1][2] = "O"
                        case 7:
                            board[2][0] = "O"
                        case 8:
                            board[2][1] = "O"
                        case 9:
                            board[2][2] = "O"
        else :
            print("Case déja occupé, veuillez chosir à nouveau")
            PVP(player, board)

def check_win(board):
    lines = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
    return None

def print_board(board):
    color_board = []
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[i][j]
            if cell == "X":
                cell = f"{RED}X{RESET}"
            elif cell == "O":
                cell = f"{BLUE}O{RESET}"
            row.append(cell)
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_possible_win(board, player):
    if player == 2:
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    x = check_win(board)
                    if x:
                        board[i][j] = " "
                        return place_to_int(i,j)
                    else:
                        board[i][j] = " "
        return 10
    else :
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    x = check_win(board)
                    if x:
                        board[i][j] = " "
                        return place_to_int(i,j)
                    else:
                        board[i][j] = " "
        return 10

def check_possible_move(board):
    possibility = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                possibility.append(place_to_int(i,j))
    x = random.randint(0,(len(possibility)-1))
    return possibility[x]

def AI(board):
    x = check_possible_win(board, 1)
    if x != 10:
        move(x, board, 2)
    else:
        y = check_possible_win(board, 2)
        if y != 10:
            move(y, board, 2)
        else:
            z = check_possible_move(board)
            move(z, board, 2)
    print("L'IA joue...")
    a = random.randint(1000, 2000)
    a = a/1000
    time.sleep(a)
    print_board(board)
    winner = check_win(board)
    if winner:
        print(f"Gagnant: {winner}")
        return
    IA(1, board)


def IA(joueur, board):
    if joueur == 1:
        x = int(input("Veuillez choisir sur quel case jouer : "))
        move(x, board, joueur)
        print_board(board)
        winner = check_win(board)
        if winner:
            print(f"Gagnant : {winner}")
            return
        else:
            joueur = joueur + 1
            if joueur == 2:
                AI(board)
            else :
                joueur = 1
                PVP(joueur, board)
    else:
        AI(board)

def PVP(joueur, board):
    x = int(input(f"Joueur {joueur}, veuillez choisir sur quel case jouer : "))
    move(x, board, joueur)
    print_board(board)
    win = check_win(board)
    if win == 1:
        return
    else:
        joueur = joueur + 1
        if joueur == 2:
            PVP(joueur, board)
        else :
            joueur = 1
            PVP(joueur, board)

def first():
    print("Ceci est le tableau avec lequel vous jouerez :")
    x = 3
    y = 3
    n = 1
    for i in range(x):
        row_values = []
        for j in range(y):
            row_values.append(str(n))
            n += 1
        print(" | ".join(row_values))
        if i < x - 1:
            print("-" * 9)
    board = [[" " for i in range(x)] for j in range(y)]
    print("Le premier joueur seras X tandit que le second joueur seras O")
    playing = int(input("Voulez vous jouer contre : 1, un IA ou 2, un autre joueur en local : "))
    if playing == 2:
        PVP(1, board)
    elif playing == 1:
        IA(1, board)
first()
