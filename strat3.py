import math
from random import randint

from strat1 import get_nb_cases

class Node:
    def __init__(self, _parent, _grid, _combinaison):
        self.parent = _parent
        self.children = []
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.visits = 0
        self.combinaison = _combinaison
        self.grid = self.place_pawn(_grid, _combinaison)
        if (get_nb_cases(self.grid) > 0):
            self.create_children()
        else:
            self.update(self.calculate_result())
    
    def create_children(self):
        combs = self.get_binaire_combinaisons()
        for i in range (len(combs)):
            self.children.append(Node(self, self.grid, combs[i]))

    def calculate_result(self):
        ia_count = 0
        j_count = 0
        for i in range(len(self.grid)):
            if (self.grid[i] == '1'):
                ia_count += 1
            elif (self.grid[i] == '2'):
                j_count += 1
        if (j_count > ia_count):
            return 1
        elif(j_count == ia_count):
            return 2
        else:
            return 0
        

    def get_value(self):
        if self.visits == 0:
            return math.inf
        value = self.get_winrate() + math.sqrt(2)*math.sqrt(math.log(self.parent.get_visits()) / self.visits)
        return value

    def get_winrate(self):
        if self.visits == 0:
            return 0
        winrate = (self.wins + self.draws) / self.visits
        return winrate
    
    def get_visits(self):
        return self.visits
    
    # result = 0 : win / result = 1 : loss / result = 2 : draw
    def update(self, result):
        if result == 0:
            self.wins += 1
        elif result == 1:
            self.losses += 1
        elif result == 2:
            self.draws += 1
        visits += 1
        if (self.parent != None):
            self.parent.update(result)
            
    # Placer les pions données par "p"
    def place_pawn(self, grid, p):
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


                