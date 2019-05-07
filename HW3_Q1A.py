import numpy as np

def moveCells(cells, p1):

    p0 = (1-p1)/2
    p2 = p0

    # a is the number of cells that renew asymmetrically
    # b is the number of cells that renew symmetrically
    a = min(cells[0], np.random.poisson(lam=(p1*cells[0])))
    b = min(cells[0], np.random.poisson(lam=(p2/(1-p1))*(cells[0]-a)))

    cells = np.array([a+2*b, cells[1]+a+2*(cells[0]-a-b)])
    return cells

TimeList = []
n = 1000 # Total number of simulation

for i in range(n):
    #print('run', i)
    t = 0
    # cells[0] and cells [1] are the number of stem cells and terminal cells respectively.
    cells = [1, 0] # Initial conditions

    while cells[0] != 0: # There are still stem cells exist
        t += 1
        #print(cells)
        cells = moveCells(cells, 0.8)

    TimeList.append(t)

print(TimeList)
print(np.median(TimeList))
