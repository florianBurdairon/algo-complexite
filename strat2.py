import math


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
    combinaisons = []

    def get_binaire_combinaisons_recur(n: int,p,i=0):
        # Cas de base : si n est égal à zéro, on n'a plus rien à faire
        if i == 2:
            combinaisons.append("".join(p))
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

    get_binaire_combinaisons_recur(n,list('0'*n))

    #Recherche des coups simple
    if(len(combinaisons) == 0 and grid.count('0')):
        p = list('0'*n)
        p[grid.find('0')] = val
        return ["".join(p)]

    return combinaisons

# print(get_binaire_combinaisons(9,'010111011',"2"));

def use_strat_2(grid: str,maxdepth = 3):
    def minmax(depth: int,maximizing:bool ,grid: str):
        # #########Debug
        # total=""
        # for itext in range(len(grid)):
        #     total += grid[itext] + ( "n" if (itext+1)%int(math.sqrt(len(grid))) == 0 else "")
        # minmax.output.append("\t"*(maxdepth-depth)+total)
        # #########Debug

    
        complet = True
        for i in range(len(grid)):
            if grid[i] == "0":
                complet = False
                break
        if(depth == 0 or complet):
            count = 0
            joueur = "2" if maximizing else "1"
            for i in range(len(grid)):
                if grid[i] == joueur:
                    count+=1
            return count
        if(maximizing):
            val = -math.inf
            for tentative in get_binaire_combinaisons(len(grid),grid,"1" if maximizing else "2"):
                choix = place_pawn(grid,tentative)
                iteration = minmax(depth-1,not maximizing,choix)
                if(iteration > val):
                    minmax.bestMove = tentative
                    val = iteration
        else:
            val = math.inf
            for tentative in get_binaire_combinaisons(len(grid),grid,"1" if maximizing else "2"):
                choix = place_pawn(grid,tentative)
                iteration = minmax(depth-1,not maximizing,choix)
                if(iteration < val):
                    val = iteration
        return val
    minmax.bestMove = ""
    minmax.output = []
    minmax(maxdepth,True,grid)
    return minmax.bestMove
    
    #########Debug
    # total = "strict graph {"
    # id = 0
    # queue = []
    # output = "\n".join(minmax.output)

    # for element in output.split("\n"):
    #     total+= str(id) + ' [label="'+element.replace("\t","").replace("n","\n")+'"] '
    #     if(len(queue) < element.count("\t")):
    #         queue.append(id-1)
    #     while(len(queue) > element.count("\t")):
    #         queue.pop()
    #     if(len(queue)):
    #         predID= queue[-1]
    #         total+= str(predID) + " -- " +str(id)+"\n"
    #     id+=1
    # total +="}"
    # print(total)
    ########Debug








