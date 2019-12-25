import random
import numpy as np

def get_rval(x):
    tmp = random.randint(0,99)
    if tmp%2:
        return random.randint(0,x-1)
    else:
        return random.randint(x+1,9)

def get_rval2(x):
    x1 = get_rval(x)
    x2 = get_rval(x)
    while abs(x1-x2)==1:
        x1 = get_rval(x)
        x2 = get_rval(x)
    return x1, x2

def get_random_occ_grid():
    row = random.randint(2,7)
    col = random.randint(2,7)

    rc1, rc2 = get_rval2(col)
    cr1, cr2 = get_rval2(row)

    occ_grid = np.ones((10,10))
    
    for i in range(10):
        if not (i==rc1 or i==rc2):
            occ_grid[row,i] = 0

        if not (i==cr1 or i==cr2):
            occ_grid[i,col] = 0
    
    return occ_grid