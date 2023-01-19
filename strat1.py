from random import randint
import math


def get_number_covered(grid: str, p: str, nb = '1'):
    width_grid = int(math.sqrt(len(grid)))
    nb_i = 0
    # Count how many points has the AI
    for i in range(len(grid)):
        if (grid[i] == nb):
            nb_i += 1
    # Play the new pawns
    m= []
    for i in range(len(grid)):
        m.append(grid[i])
    for i in range(len(p)):
        if (p[i] == nb):
            m[i] = nb
            if (i%width_grid != width_grid-1):
                m[i+1] = nb
            if (i%width_grid != 0):
                m[i-1] = nb
            if (i>=width_grid):
                m[i - width_grid] = nb
            if (i < width_grid*width_grid - width_grid):
                m[i + width_grid] = nb
    # Count how many points has the AI after playing
    new_nb_i = 0
    for i in range(len(m)):
        if (m[i] == nb):
            new_nb_i += 1
    # Return the number of points added with this pawn placement
    return new_nb_i - nb_i

#Stratégie 1
combinaisons = []

# Récupérer les combinaisons jouables
def get_binaire_combinaisons(n: int,p = "",i=0):
    # Cas de base : si n est égal à zéro, on n'a plus rien à faire
    if i == 2:
        combinaisons.append("".join(p))
        return
    if n == 0:
        return
    # Sinon, on affiche la combinaison binaire courante et on appelle récursivement la fonction
    # en diminuant n de 1
    if(p[n-1] == "0"):
        str0 = list(p)
        str0[n-1] = "0"
        get_binaire_combinaisons(n - 1,str0 ,i)
        i+=1; 
    str1 = list(p)
    str1[n-1] = "1"
    get_binaire_combinaisons(n - 1,str1 ,i)

# Retourne le nombre de cases qu'il reste à remplir
def get_nb_cases(grid: str, val = '0'):
    nb_cases = 0
    for i in range(len(grid)):
        if (grid[i] == val):
            nb_cases = nb_cases + 1
    return nb_cases

def use_strat_1(grid: str):
    global combinaisons

    best_combs = []

    combinaisons = []
    max_ = 0 # Maximal new points
    best_mov = "" # Pawns placement for minimal number
    nb_cases = get_nb_cases(grid)
    get_binaire_combinaisons(nb_cases,"0"*nb_cases)
    for i in range(len(combinaisons)):
        comb = ""
        ind = 0
        for j in range(len(grid)):
            if(grid[j] == '0'):
                comb = comb + combinaisons[i][ind]
                ind = ind + 1
            else:
                comb = comb + "0"
        combinaisons[i] = comb
        nb_new_cases = get_number_covered(grid, comb)
        if max_ < nb_new_cases:
            max_ = nb_new_cases
    
    for i in range(len(combinaisons)):
        if (get_number_covered(grid, combinaisons[i]) == max_):
            best_combs.append(combinaisons[i])
        
    alea = randint(0, len(best_combs)-1)
    best_mov = best_combs[alea]
    
    return best_mov