from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import constants as c
import numpy as np
import plot
import matplotlib.pyplot as plt

plots = []
# for i in range(12):
#     print(i, i, i)
#     random.seed(i)
#     np.random.seed(i)
#     phc = PARALLEL_HILL_CLIMBER()
#     phc.Evolve()
#     # phc.Show_Best()
#     phc.Save_Best()
#     p = phc.plot()
#     plots.append(p)
random.seed(2)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
# phc.Show_Best()
phc.Save_Best()
p = phc.plot()
plots.append(p)
input("Press Enter to Continue")
for b in phc.bests:
    b.Start_Simulation("GUI")
for pl in plots:
    fig = plt.figure()
    fig.axes.append(pl)
    plt.show()


