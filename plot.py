import solution
import matplotlib.pyplot as plt
import numpy as np
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import random
import time as time
import constants as c

# Plot the fitness of the best solution in each generation
def plot_fitness():
    plt.plot(solution.fitness)
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness of Best Solution in Each Generation')
    plt.show()

