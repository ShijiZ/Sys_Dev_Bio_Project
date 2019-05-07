import numpy as np
import matplotlib.pyplot as plt

def moveCells(cells, p1, pd, g):

    p0 = (1-p1)/2
    p2 = p0

    # a is the number of cells that renew asymmetrically
    # b is the number of cells that renew symmetrically
    # c is the number of terminal cells die in each cell cycle
    a = min(cells[0], np.random.poisson(lam=(p1*cells[0])))
    b = min(cells[0], np.random.poisson(lam=(p2/(1-p1))*(1/(1+g*cells[0]))*(cells[0]-a)))
    c = min(cells[1], np.random.poisson(lam=(pd*cells[1])))

    cells = np.array([a+2*b, max(0, cells[1]+a+2*(cells[0]-a-b)-c)])
    return cells

StepStemCellsList = []
StepTerminalCellsList = []
n = 1000 # Total number of simulation

for i in range(n):
    t = 0
    # cells[0] and cells [1] are the number of stem cells and terminal cells respectively.
    cells = [12, 12] # Initial conditions
    StepStemCells = [12]
    StepTerminalCells = [12]

    while t <= 200: # cell cycles simulated
        t += 1
        #print(cells)
        cells = moveCells(cells, 0.2, 0.1, 0.0001)
        StepStemCells.append(cells[0])
        StepTerminalCells.append(cells[1])

    StepStemCellsList.append(StepStemCells)
    StepTerminalCellsList.append(StepTerminalCells)

# This list contains t+1 sublist storing the number of
# stem cells at each cell cycle for each simulation.
StemCellCycleList =[]
for j in range(t+1):
    StemCellCycleList.append([])

    for i in StepStemCellsList:
        StemCellCycleList[j].append(i[j])

# These 2 list store the means and variances of the number of
# stem cells at each cell cycle for each simulation.
MeanStemCellList = []
VarianceStemCellList = []
for i in StemCellCycleList:
    MeanStemCellList.append(np.mean(i))
    VarianceStemCellList.append(np.var(i))

#plt.figure(1)
#plt.plot(range(t+1), StepStemCellsList[0], range(t+1), StepStemCellsList[1],
#         range(t+1), StepStemCellsList[2], range(t+1), StepStemCellsList[3],
#         range(t+1), StepStemCellsList[4], range(t+1), StepStemCellsList[5],
#         range(t+1), StepStemCellsList[6], range(t+1), StepStemCellsList[7],
#         range(t+1), StepStemCellsList[8], range(t+1), StepStemCellsList[9])
#plt.xlabel('cell cycle')
#plt.ylabel('Number of Stem Cells')
#plt.figure(2)
#plt.plot(range(t+1), StepTerminalCellsList[0], range(t+1), StepTerminalCellsList[1],
#         range(t+1), StepTerminalCellsList[2], range(t+1), StepTerminalCellsList[3],
#         range(t+1), StepTerminalCellsList[4], range(t+1), StepTerminalCellsList[5],
#         range(t+1), StepTerminalCellsList[6], range(t+1), StepTerminalCellsList[7],
#         range(t+1), StepTerminalCellsList[8], range(t+1), StepTerminalCellsList[9])
#plt.xlabel('cell cycle')
#plt.ylabel('Number of Terminal Cells')
plt.figure(3)
plt.plot(range(t+1), MeanStemCellList)
plt.ylim(0, 20)
plt.xlabel('cell cycle')
plt.ylabel('Mean Value of the Number of Stem Cells')
plt.figure(4)
plt.plot(range(t+1), VarianceStemCellList)
plt.xlabel('cell cycle')
plt.ylabel('Variance of the Number of Stem Cells')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.show()
