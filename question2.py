minimal = 16 # Minimal number of points
winner = "" # Points position for minimal number

# Can the position of points cover the whole grid
def can_be_covered(p: str):
    m = []
    verif = []
    for i in range(len(p)):
        m.append(p[i])
        verif.append('1')
    for i in range(len(p)):
        if (p[i] == '1'):
            if (i%4 != 3):
                m[i+1] = '1'
            if (i%4 != 0):
                m[i-1] = '1'
            if (i>=4):
                m[i - 4] = '1'
            if (i < 12):
                m[i + 4] = '1'
    if (m == verif):
        return True
    return False

# Return the number of points to cover everything if possible to cover everything, else return 0
def get_points_to_cover_all(p: str):
    points = 0
    if (can_be_covered(p)):
        for i in range(len(p)):
            if (p[i] == '1'):
                points += 1
    return points

# Calculate the minimal number of points and their disposition
def calc_minimal_points_to_cover_all(n: int, str: str = ""):
    global minimal, winner
    if n == 0:
        i = get_points_to_cover_all(str)
        if (i < minimal and i != 0):
            minimal = i
            winner = str
        return
    
    str0 = str + "0"
    calc_minimal_points_to_cover_all(n - 1, str0)
    str1 = str + "1"
    calc_minimal_points_to_cover_all(n - 1, str1)

calc_minimal_points_to_cover_all(16)
print(minimal)
print(winner)