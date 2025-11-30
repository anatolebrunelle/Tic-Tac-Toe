import random
import time
import sys
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

def place_to_int(y, x):
    return y * 3 + x + 1


def int_to_place(x, board):
    row = (x - 1) // 3
    col = (x - 1) % 3
    return board[row][col]



def move(x, board, player, playing):
    if x < 1 or x > 9:
        print("Veuillez choisir un nombre valide.")
        if playing == 1:
            IA(player, board)
        else:
            PVP(player, board)
        return

    row = (x - 1) // 3
    col = (x - 1) % 3

    if board[row][col] == " ":
        board[row][col] = "X" if player == 1 else "O"
    else:
        print("Case déjà occupée, veuillez choisir à nouveau.")
        if playing == 1:
            IA(player, board)
        else:
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

def check_full(board):
    a = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                a = a + 1
    if a == 9:
        return True
    else :
        return False

def AI(board):
    x = check_possible_win(board, 1)
    if x != 10:
        move(x, board, 2, 1)
        if check_full(board):
            print("Le plateau est plein, c'est une égalité.")
            sys.exit()
    else:
        y = check_possible_win(board, 2)
        if y != 10:
            move(y, board, 2, 1)
            if check_full(board):
                print("Le plateau est plein, c'est une égalité.")
                sys.exit()
        else:
            z = check_possible_move(board)
            move(z, board, 2, 1)
            if check_full(board):
                print("Le plateau est plein, c'est une égalité.")
                sys.exit()
    print("L'IA joue...")
    a = random.randint(1000, 2000)
    a = a/1000
    time.sleep(a)
    print_board(board)
    winner = check_win(board)
    if winner:
        print(f"Gagnant : {winner}")
        return
    IA(1, board)


def IA(joueur, board):
    if joueur == 1:
        x = input("Veuillez choisir sur quelle case jouer : ")
        if x.lower() =="rappel":
            rappel(1, joueur, board)
        else :
            x = int(x)
            move(x, board, joueur, 1)
            print_board(board)
            if check_full(board):
                print("Le plateau est plein, c'est une égalité.")
                sys.exit()
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
    x = input(f"Joueur {joueur}, veuillez choisir sur quelle case jouer : ")
    if x.lower() =="rappel":
        rappel(2, joueur, board)
    else:
        x = int(x)
        move(x, board, joueur, 2)
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

def rappel(play, joueur, board):
    print("Voici le plateau avec lequel vous jouez :")
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
    if play == 1:
        IA(joueur, board)
    elif play == 2:
        PVP(joueur, board)
    else:
        return
    
def first():
    rappel(0, 1, ["hello"])
    x = 3
    y = 3
    board = [[" " for i in range(x)] for j in range(y)]
    print("Le premier joueur sera X tandis que le second joueur sera O.")
    print('Vous pouvez écrire "rappel" pour afficher les numéros des cases du plateau.')
    playing = int(input("Voulez-vous jouer contre : 1 — une IA, ou 2 — un autre joueur en local : "))
    if playing == 2:
        PVP(1, board)
    elif playing == 1:
        IA(1, board)
first()
