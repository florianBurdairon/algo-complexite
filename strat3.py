import math
from random import randint

from strat1 import get_nb_cases

# Récupérer les combinaisons jouables
def get_binaire_combinaisons(n: int,p = "", val="1"):
    def get_binaire_combinaisons_recur(n: int,p = "",i=0):
        # Cas de base : si n est égal à zéro, on n'a plus rien à faire
        if i == 2:
            get_binaire_combinaisons_recur.combinaisons.append("".join(p))
            return
        if n == 0:
            return
        # Sinon, on affiche la combinaison binaire courante et on appelle récursivement la fonction
        # en diminuant n de 1
        str1 = list(p)

        if(p[n-1] == "0"):
            str0 = list(p)
            str0[n-1] = "0"
            get_binaire_combinaisons_recur(n - 1,str0 ,i)
            i+=1
            str1[n-1] = val
        get_binaire_combinaisons_recur(n - 1,str1 ,i)

    get_binaire_combinaisons_recur.combinaisons = []
    get_binaire_combinaisons_recur(n,p)
    return get_binaire_combinaisons_recur.combinaisons


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



def use_strat_3(grid:str):
    width = math.sqrt(len(grid))
    best_mov = ""
    best_moves = []

    nb_cases = get_nb_cases(grid)

    # Get every combinaisons at depth 1
    combs = get_binaire_combinaisons(nb_cases, "0"*nb_cases)
    grids = []
    val = []

    maximum = 0
    index_max = -1

    # For each comb : 
    for ind in range(len(combs)):
        # We rewrite it correctly for the grid
        c = ""
        i = 0
        for j in range(len(grid)):
            if(grid[j] == '0'):
                c = c + combs[ind][i]
                i = i + 1
            else:
                c = c + "0"
        combs[ind] = c

        # All grids with pawn placement
        grids.append(place_pawn(grid, c))
        # Get value for this branch
        val.append(mcts_recursive(grids[ind], "1"))
    
    maximum = 0.0

    for i in range(len(val)):
        if (float(val[i][0]) / float(val[i][1]) > maximum):
            maximum = float(val[i][0]) / float(val[i][1])

    best_combs = []
    for i in range(len(val)):
        if (float(val[i][0])/float(val[i][1]) == maximum):
            best_combs.append(combs[i])
    
    # Use the best move
    best_mov = best_combs[randint(0, len(best_combs)-1)]
    return best_mov

def mcts_recursive(grid:str, p:str):
    # Fin de partie :
    if get_nb_cases(grid) == 0:
        ia_count = 0
        j_count = 0
        for i in range(len(grid)):
            if (grid[i] == '1'):
                ia_count += 1
            elif (grid[i] == '2'):
                j_count += 1
        if ia_count > j_count:
            return [1, 1]
        else:
            return [0, 1]
    else:
        nb_cases = get_nb_cases(grid)

        # Get every combinaisons at depth 1
        combs = get_binaire_combinaisons(nb_cases, "0"*nb_cases, p)
        rets = []

        if (len(combs) > 0):
            # For each comb : 
            for ind in range(len(combs)):
                # We rewrite it correctly for the grid
                c = ""
                i = 0
                for j in range(len(grid)):
                    if(grid[j] == '0'):
                        c = c + combs[ind][i]
                        i = i + 1
                    else:
                        c = c + "0"
                #combs[ind] = c

                # Get value for this branch
                rets.append(mcts_recursive(place_pawn(grid, c), "2" if p=="1" else "1"))

            sum_victory = 0
            sum_game = 0
            for i in range(len(rets)):
                sum_victory += rets[i][0]
                sum_game += rets[i][1]
            
            if sum_game == 0: print(len(rets))
            return [sum_victory, sum_game]
        return [0, 1]
                