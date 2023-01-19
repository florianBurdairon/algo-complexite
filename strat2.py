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
def get_binaire_combinaisons(n: int,grid = "", val="1"):
    def get_binaire_combinaisons_recur(n: int,p,i=0):
        # Cas de base : si n est égal à zéro, on n'a plus rien à faire
        if i == 2:
            get_binaire_combinaisons_recur.combinaisons.append("".join(p))
            return
        if n == 0:
            return
        # Sinon, on affiche la combinaison binaire courante et on appelle récursivement la fonction
        # en diminuant n de 1
        str1 = p.copy()

        if(grid[n-1] == "0"):
            str0 = p.copy()
            get_binaire_combinaisons_recur(n - 1,str0 ,i)
            i+=1
            str1[n-1] = val
        get_binaire_combinaisons_recur(n - 1,str1 ,i)

    get_binaire_combinaisons_recur.combinaisons = []
    get_binaire_combinaisons_recur(n,list('0'*n))
    return get_binaire_combinaisons_recur.combinaisons

# print(get_binaire_combinaisons(5,'00200'));



def use_strat_2(depth: int,maximizing:bool ,grid: str):
   
    complet = True
    for i in range(len(grid)):
        if grid[i] == "0":
            complet = False
            break
    print(depth,complet)
    if(depth == 0 or complet):
        #########Debug
        # print(depth,complet)
        # print("----")
        # total=""
        # for itext in range(len(grid)):
        #     total += grid[itext] + ( "\n" if (itext+1)%int(math.sqrt(len(grid))) == 0 else "")
        # print(total)
        #########Debug
        return 

    for tentative in get_binaire_combinaisons(len(grid),grid,"1" if maximizing else "2"):
        choix = place_pawn(grid,tentative)
        print(tentative)
        print("----")
        total=""
        for itext in range(len(choix)):
            total += choix[itext] + ( "\n" if (itext+1)%int(math.sqrt(len(choix))) == 0 else "")
        print(total)
        use_strat_2(depth-1,not maximizing,choix);
    
use_strat_2(3,True,"0"*9)


