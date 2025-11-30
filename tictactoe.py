RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"


def int_to_place(x, board):
    match x:
        case 1:
            return board[0][0]
        case 2:
            return board[0][1]
        case 3:
            return board[0][2]
        case 4:
            return board[1][0]
        case 5:
            return board[1][1]
        case 6:
            return board[1][2]
        case 7:
            return board[2][0]
        case 8:
            return board[2][1]
        case 9:
            return board[2][2] 


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
                            board[0][0] = f"{RED}X{RESET}"
                        case 2:
                            board[0][1] = f"{RED}X{RESET}"
                        case 3:
                            board[0][2] = f"{RED}X{RESET}"
                        case 4:
                            board[1][0] = f"{RED}X{RESET}"
                        case 5:
                            board[1][1] = f"{RED}X{RESET}"
                        case 6:
                            board[1][2] = f"{RED}X{RESET}"
                        case 7:
                            board[2][0] = f"{RED}X{RESET}"
                        case 8:
                            board[2][1] = f"{RED}X{RESET}"
                        case 9:
                            board[2][2] = f"{RED}X{RESET}"
                case 2:
                    match x:
                        case 1:
                            board[0][0] = f"{BLUE}O{RESET}"
                        case 2:
                            board[0][1] = f"{BLUE}O{RESET}"
                        case 3:
                            board[0][2] = f"{BLUE}O{RESET}"
                        case 4:
                            board[1][0] = f"{BLUE}O{RESET}"
                        case 5:
                            board[1][1] = f"{BLUE}O{RESET}"
                        case 6:
                            board[1][2] = f"{BLUE}O{RESET}"
                        case 7:
                            board[2][0] = f"{BLUE}O{RESET}"
                        case 8:
                            board[2][1] = f"{BLUE}O{RESET}"
                        case 9:
                            board[2][2] = f"{BLUE}O{RESET}"
        else :
            print("Case déja occupé, veuillez chosir à nouveau")
            main(player, board)

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
            print(f"Winner: {line[0]}")
            return 1
    return 0

    

def print_board(board):
    x = 3
    y = 3
    for i in range(x):
        row = " | ".join(str(board[i][j]) for j in range(y))
        print(row)
        if i < x - 1:
            print("-" * 9)

def main(joueur, board):
    x = int(input(f"Joueur {joueur}, veuillez choisir sur quel case jouer : "))
    move(x, board, joueur)
    print_board(board)
    win = check_win(board)
    if win == 1:
        return
    else:
        joueur = joueur + 1
        if joueur == 2:
            main(joueur, board)
        else :
            joueur = 1
            main(joueur, board)

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
    main(1, board)

first()