import os
import generate
import simulate
from hillclimber import HILL_CLIMBER

#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

hc = HILL_CLIMBER()
hc.Evolve()

# for _ in range(5):
#     generate.fun_g()
#     simulate.fun_s()