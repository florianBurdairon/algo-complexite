import math
from random import randint

from strat1 import get_nb_cases

class Node:
    def __init__(self, _grid, _parent = None, _combinaison = None):
        self.parent = _parent
        self.children = []
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.visits = 0
        self.combinaison = _combinaison
        if _combinaison != None:
            self.grid = self.place_pawn(_grid)
        else:
            self.grid = _grid
        if get_nb_cases(self.grid) > 0:
            self.create_children()
    
    def create_children(self):
        val = '1'
        if (self.combinaison != None):
            if ('1' in self.combinaison): # Next player is human (since this node is AI)
                val = '2'
        
        g_mod = '0' * get_nb_cases(self.grid)
        combs = self.get_binaire_combinaisons(len(g_mod), g_mod, val)

        for x in range(len(combs)):
            comb = ""
            ind = 0
            for j in range(len(self.grid)):
                if(self.grid[j] == '0'):
                    comb = comb + combs[x][ind]
                    ind = ind + 1
                else:
                    comb = comb + "0"
            combs[x] = comb

        for i in range (len(combs)):
            self.children.append(Node(self.grid, self, combs[i]))

    def look_in_once(self):
        if len(self.children) > 0:
            # Get maximum
            max = 0
            for c in self.children:
                if c.get_value() > max:
                    max = c.get_value()
            # Get array of all maximum
            maximums = []
            for c in self.children:
                if c.get_value() == max:
                    maximums.append(c)
            # Choose random in it
            chosen = maximums[randint(0, len(maximums) - 1)]
            chosen.look_in_once()
        else:
            self.update(self.calculate_result())

    def calculate_result(self):
        ia_count = get_nb_cases(self.grid, '1')
        j_count = get_nb_cases(self.grid, '2')
        if (j_count > ia_count):    # Loss
            return 1
        elif(j_count == ia_count):  # Draw
            return 2
        else:   # Win
            return 0

    def get_value(self):
        if self.visits == 0:
            return math.inf
        if (self.parent != None):
            value = self.get_winrate() + math.sqrt(2)*math.sqrt(math.log(self.parent.get_visits()) / self.visits)
            return value
        else:
            return 0

    def get_winrate(self):
        if self.visits == 0:
            return 0
        winrate = (self.wins + self.draws) / self.visits
        return winrate
    
    def get_visits(self):
        return self.visits

    def get_combinaison(self):
        return self.combinaison
    
    # result = 0 : win / result = 1 : loss / result = 2 : draw
    def update(self, result):
        if result == 0:
            self.wins += 1
        elif result == 1:
            self.losses += 1
        elif result == 2:
            self.draws += 1
        self.visits += 1
        if (self.parent != None):
            self.parent.update(result)
            
    # Placer les pions données par "p"
    def place_pawn(self, _grid):
        width_grid = int(math.sqrt(len(_grid)))
        newgrid = []
        for i in range (len(_grid)):
            newgrid.append(_grid[i])
        for i in range (len(_grid)):
            if (self.combinaison[i] != '0'):
                newgrid[i] = self.combinaison[i]
                if (i%width_grid < width_grid-1):
                    newgrid[i+1] = self.combinaison[i]
                if (i%width_grid != 0):
                    newgrid[i-1] = self.combinaison[i]
                if (i>=width_grid):
                    newgrid[i - width_grid] = self.combinaison[i]
                if (i < width_grid*width_grid - width_grid):
                    newgrid[i + width_grid] = self.combinaison[i]
        strgrid = ""
        for i in range(len(newgrid)):
            strgrid += newgrid[i]
        return strgrid

    # Récupérer les combinaisons jouables 
    def get_binaire_combinaisons(self, n: int,grid, val="1"):
        combinaisons = []
        def get_binaire_combinaisons_recur(n2: int,p,i=0):
            # Cas de base : si n est égal à zéro, on n'a plus rien à faire
            if i == 2:
                combinaisons.append(p.copy())
                return
            if n2 == 0:
                return
            # Sinon, on affiche la combinaison binaire courante et on appelle récursivement la fonction
            # en diminuant n de 1
            if(grid[n2-1] == '0'):
                get_binaire_combinaisons_recur(n2 - 1,p ,i)
                p[n2-1] = val
                get_binaire_combinaisons_recur(n2 - 1,p ,i+1)
                p[n2-1] = '0'
            else:
                get_binaire_combinaisons_recur(n2 - 1,p ,i)
        
        if(get_nb_cases(self.grid) > 2):
            get_binaire_combinaisons_recur(n,list(grid))
        else:
            p =  ['0'] * len(grid)
            for i in range(len(grid)):
                if(grid[i] == '0'):
                    p[i] =  val
            return [p]
        return combinaisons

    def get_best_move(self):
        max_winrate = 0
        best_move = None
        for child in self.children:
            if child.get_winrate() >= max_winrate:
                max_winrate = child.get_winrate()
                best_move = child.get_combinaison()
        return best_move

def use_strat_3(grid:str):
    print("Creating base model for simulation...")
    root = Node(grid)
    
    print("Starting simulation...")
    #Start LOTS OF simulations :
    for i in range(20000):
        root.look_in_once()

    bm = root.get_best_move()

    return bm
