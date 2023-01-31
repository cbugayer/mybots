
import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random
import time as time
import constants as c
from simulation import SIMULATION
import sys

# def fun_s():
#     simulation = SIMULATION()
#     simulation.Run()
#     simulation.Get_Fitness()
# fun_s()
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
simulation.Get_Fitness()
