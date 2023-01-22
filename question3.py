import math
from random import randint

from strat1 import use_strat_1, get_nb_cases
from strat2 import use_strat_2
from strat3 import use_strat_3


# Placer les pions données par "p"
def place_pawn(grid, p):
    width_grid = int(math.sqrt(len(grid)))
    newgrid = []
    for i in range (len(grid)):
        newgrid.append(grid[i])
    for i in range (len(grid)):
        if (p[i] != '0'):
            newgrid[i] = p[i]
            if (i%width_grid < width_grid-1):
                newgrid[i+1] = p[i]
            if (i%width_grid != 0):
                newgrid[i-1] = p[i]
            if (i>=width_grid):
                newgrid[i - width_grid] = p[i]
            if (i < width_grid*width_grid - width_grid):
                newgrid[i + width_grid] = p[i]

    strgrid = ""
    for i in range(len(newgrid)):
        strgrid += newgrid[i]
    return strgrid

# Afficher la grille
def display_grid(grid):
    width_grid = int(math.sqrt(len(grid)))
    first = "    "
    for i in range(width_grid):
        first += "" + str(i) + " "
    print(first + "\n")
    for i in range(width_grid):
        line = "" + str(i) + "   "
        for ii in range(width_grid):
            c = grid[i*width_grid+ii]
            if (c == '0'):
                line += "- "
            elif(c == '1'):
                line += 'O '
            else:
                line += 'X '
        print(line)
        
    ia_count = 0
    j_count = 0
    for i in range(len(grid)):
        if (grid[i] == '1'):
            ia_count += 1
        elif (grid[i] == '2'):
            j_count += 1
    print("Vous : " + str(j_count) + ", IA : " + str(ia_count))

# Demander des coordonnées correctes
def get_correct_input(width_grid, txt):
    x = -1
    while (x < 0 or x >= width_grid):
        x_str = input("Entrer la coordonnée" + txt + " : ")
        if (x_str != ''):
            x = int(x_str)
    return x

# Tour du joueur
def player_play(grid):
    width_grid = int(math.sqrt(len(grid)))

    x1 = get_correct_input(width_grid, " X du premier point")
    y1 = get_correct_input(width_grid, " Y du premier point")

    while (grid[x1 + y1*width_grid] != '0'):
        print("Impossible de jouer ici")
        x1 = get_correct_input(width_grid, " X du premier point")
        y1 = get_correct_input(width_grid, " Y du premier point")

    x2 = -1
    y2 = -1
    if (get_nb_cases(grid) > 1):
        x2 = get_correct_input(width_grid, " X du second point")
        y2 = get_correct_input(width_grid, " Y du second point")
        while (grid[x2 + y2*width_grid] != '0' or (x1 == x2 and y1 == y2)):
            print("Impossible de jouer ici")
            x2 = get_correct_input(width_grid, " X du second point")
            y2 = get_correct_input(width_grid, " Y du second point")

    p = ""
    for i in range(len(grid)):
        if (i == x1 + y1 * width_grid or i == x2 + y2 * width_grid):
            p += '2'
        else:
            p += '0'
    return p


# Lancement de la partie
def play(width_grid: int, strat: int):
    # Generate empty grid
    grid = ""
    for i in range(width_grid):
        for i in range(width_grid):
            grid += '0'
    
    while get_nb_cases(grid) != 0:
        display_grid(grid)
        p_j = player_play(grid)
        grid = place_pawn(grid, p_j)
        print("\nVous avez joué : ")
        display_grid(grid)
        if (get_nb_cases(grid) != 0):
            p_ia = get_comb_ia(grid, strat)
            grid = place_pawn(grid, p_ia)
            print("\nL'IA a joué : ")
    
    display_grid(grid)

    ia_count = 0
    j_count = 0
    for i in range(len(grid)):
        if (grid[i] == '1'):
            ia_count += 1
        elif (grid[i] == '2'):
            j_count += 1
    if (j_count > ia_count):
        print("Vous avez gagné !")
    elif(j_count == ia_count):
        print("Egalité ! Dommage...")
    else:
        print("Vous avez perdu !")



# Retourne le meilleur placement de 2 pions
def get_comb_ia(grid: str, strat: int):
    if strat == 1:
        best_mov = use_strat_1(grid)
    elif strat == 2:
        best_mov = use_strat_2(grid)
    elif strat == 3:
        best_mov = use_strat_3(grid)

    return best_mov



width = int(input("\n Entrer la taille de grille souhaitée (recommandée entre 3 et 5) : "))
strat = int(input(" Choisissez votre mode d'IA :\n  1 = Tout par tour (Stratégie 1) \n  2 = minimax (Stratégie 2) \n  3 = Monte Carlo (Stratégie 3)\n Votre choix : "))

play(width, strat)

