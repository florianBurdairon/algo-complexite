import math
from strat1 import get_nb_cases
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

# Récupérer les combinaisons jouables 
def get_binaire_combinaisons(n: int,grid:list, val="1"):
    combinaisons = []
    def get_binaire_combinaisons_recur(n: int,p:list,i=0):
        # Cas de base : si n est égal à zéro, on n'a plus rien à faire
        if i == 2:
            combinaisons.append(p.copy())
            return
        if n == 0:
            return
        # Sinon, on affiche la combinaison binaire courante et on appelle récursivement la fonction
        # en diminuant n de 1
        if(grid[n-1] == '0'):
            get_binaire_combinaisons_recur(n - 1,p ,i)
            p[n-1] = val
            get_binaire_combinaisons_recur(n - 1,p ,i+1)
            p[n-1] = '0'
        else:
            get_binaire_combinaisons_recur(n - 1,p ,i)
    if( get_nb_cases(grid) > 2):
        get_binaire_combinaisons_recur(n,list(grid))
    else:
        p =  ['0'] * len(grid)
        for i in range(len(grid)):
            if(grid[i] == '0'):
                p[i] =  val
        return [p]
    return combinaisons

def use_strat_2(grid: str,maxdepth = 3):
    def minmax(depth: int,maximizing:bool ,grid: str,alpha:int,beta:int):
        complet = True
        for i in range(len(grid)):
            if grid[i] == "0":
                complet = False
                break
        if(depth == 0 or complet):
            count = 0
            for i in range(len(grid)):
                if grid[i] == "1":
                    count+=1
            return count
        if(maximizing):
            val = -math.inf
            for tentative in get_binaire_combinaisons(len(grid),grid,"1"):
                choix = place_pawn(grid,tentative)
                iteration = minmax(depth-1,True,choix,alpha,beta)
                if(iteration > val):
                    if(maxdepth == depth):
                        minmax.bestMove = tentative
                    val = iteration
                if(val > beta):
                    break
                alpha = max(alpha,val)
        else:
            val = math.inf
            for tentative in get_binaire_combinaisons(len(grid),grid,"2"):
                choix = place_pawn(grid,tentative)
                val = min(val,minmax(depth-1,False,choix,alpha,beta))
                if val < alpha:
                    break 
                beta = min(beta, val)
        return val
    minmax.bestMove = ""
    minmax(maxdepth,True,grid, -math.inf,math.inf)
    return minmax.bestMove






