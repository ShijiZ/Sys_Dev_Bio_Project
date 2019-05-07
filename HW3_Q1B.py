import numpy as np
import matplotlib.pyplot as plt

def moveCells(cells, p1):

    p0 = (1-p1)/2
    p2 = p0

    # a is the number of cells that renew asymmetrically
    # b is the number of cells that renew symmetrically
    a = min(cells[0], np.random.poisson(lam=(p1*cells[0])))
    b = min(cells[0], np.random.poisson(lam=(p2/(1-p1))*(cells[0]-a)))

    cells = np.array([a+2*b, cells[1]+a+2*(cells[0]-a-b)])
    return cells

TimeMedianList = []
p1List = np.arange(0, 0.99, 0.01)

for p1 in p1List:
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
            cells = moveCells(cells, p1)

        TimeList.append(t)

    print(np.median(TimeList))
    TimeMedianList.append(np.median(TimeList))

plt.plot(p1List, TimeMedianList)
plt.xlabel('The probability of asymmetric division')
plt.ylabel('The median time to extinction')
plt.show()
