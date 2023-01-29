
import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random
import time as time
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()
simulation.Get_Fitness()
