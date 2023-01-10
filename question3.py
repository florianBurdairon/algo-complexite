import math

def get_number_covered(grid: str, p: str):
    width_grid = math.sqrt(len(grid))
    nb_i = 0
    # Count how many points has the AI
    for i in range(len(grid)):
        if (grid[i] == '1'):
            nb_i += 1
    # Play the new pawns
    m= []
    for i in range(len(grid)):
        m.append(grid[i])
    for i in range(len(p)):
        if (p[i] == '1'):
            m[i] = '1'
            if (i%width_grid != width_grid-1):
                m[i+1] = '1'
            if (i%width_grid != 0):
                m[i-1] = '1'
            if (i>=width_grid):
                m[i - width_grid] = '1'
            if (i < width_grid*width_grid - width_grid):
                m[i + width_grid] = '1'
    # Count how many points has the AI after playing
    new_nb_i = 0
    for i in range(len(m)):
        if (m[i] == '1'):
            new_nb_i += 1
    # Return the number of points added with this pawn placement
    return new_nb_i - nb_i

def get_covered_from_2_points(grid: str, p: str):
    nb_1 = 0
    # Remove combinaisons with more than 2 points to place
    for i in range(len(p)):
        if (p[i] == '1'):
            nb_1 += 1
    if (nb_1 == 2):
        # Remove combinaisons where we can't place at least one point
        for i in range(len(grid)):
            if (grid[i] != '0' and p[i] == '1'):
                nb_1 -= 1
        if (nb_1 == 2):
            nb_cov = get_number_covered(grid, p)
            return nb_cov
        else:
            return 0
    else:
        return 0


#Stratégie 1
combinaisons = []
def get_binaire_combinaisons(n: int, str: str = ""):
    global combinaisons
    # Cas de base : si n est égal à zéro, on n'a plus rien à faire
    if n == 0:
        combinaisons.append(str)
        return
    
    # Sinon, on affiche la combinaison binaire courante et on appelle récursivement la fonction
    # en diminuant n de 1
    str0 = str + "0"
    get_binaire_combinaisons(n - 1, str0)
    str1 = str + "1"
    get_binaire_combinaisons(n - 1, str1)
    
def get_nb_cases(grid: str):
    nb_cases = 0
    for i in range(len(grid)):
        if (grid[i] == '0'):
            nb_cases = nb_cases + 1
    return nb_cases

def get_possible_playable_combinaisons(grid: str):
    global combinaisons
    combinaisons = []
    max_ = 0 # Maximal new points
    best_mov = "" # Pawns placement for minimal number
    nb_cases = get_nb_cases(grid)
    get_binaire_combinaisons(nb_cases)
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
        nb_new_cases = get_covered_from_2_points(grid, comb)
        if max_ < nb_new_cases:
            max_ = nb_new_cases
            best_mov = comb
            
    return best_mov

def place_pawn(grid, p):
    newgrid = []
    for i in range (len(grid)):
        newgrid = grid[i]
    
        if (p[i] == 1):
            
    return newgrid

def play(width_grid: int):
    while get_nb_cases(grid) != 0:
        # Generate empty grid
        grid = ""
        for i in range(width_grid*width_grid):
            grid += '0'
        print(get_possible_playable_combinaisons(grid))



play(4)

