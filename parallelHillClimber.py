from solution import SOLUTION
import constants as c
import copy
import os
import matplotlib.pyplot as plt
import numpy as np

class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del world*.sdf")
        os.system("del body*.urdf")
        self.parents = {}
        self.fitness_arry = []
        self.bests = []
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        

    def Evolve(self):
        
        self.Evaluate(self.parents)
        
        # self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):

        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

        self.Print()
        
        self.Select()
             

    def Spawn(self):
        
        self.children = {}
        for p in self.parents.keys():
            self.children[p] = copy.deepcopy(self.parents[p])
            self.children[p].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()
        

    def Select(self):
        for p in self.parents.keys():
            if abs(self.parents[p].fitness) < abs(self.children[p].fitness):
                self.parents[p] = self.children[p]

    def Print(self):
        print("\n")
        for p in self.parents.keys():
            print(self.parents[p], self.children[p])
        print("\n")

    def Show_Best(self):
        fit = {}
        for p in self.parents.values():
            fit[p] = abs(p.fitness)
        print(fit)
        top = max(fit, key=fit.get)
        print(top.fitness)
        top.Start_Simulation("GUI")
        
        
    def Save_Best(self):
        fit = {}
        for p in self.parents.values():
            fit[p] = p.fitness
        print(fit)
        top = max(fit, key=fit.get)
        print(top.fitness)
        self.bests.append(top)

    def Show_Bests(self):
        for b in self.bests:
            b.Start_Simulation("GUI")

    def Evaluate(self,solutions):
        for pc in solutions.values():
            pc.Start_Simulation("DIRECT")
        for pc in solutions.values():
            pc.Wait_For_Simulation_To_End()
            self.fitness_arry.append(pc.Compute_Fitness())


    def plot(self):
        max_pop_fit = []
        max_for_gen = []
        for i in range(0, len(self.fitness_arry), c.populationSize):
            max_pop_fit.append(max(self.fitness_arry[i:i+c.populationSize]))
        for i in range(len(max_pop_fit)):
            max_for_gen.append(max(max_pop_fit[:i+1]))
        num_gen = np.arange(0, c.numberOfGenerations+1)
        print("\n", max_pop_fit)
        # print(num_gen, self.fitness_arry)
        fig = plt.figure()
        plt.plot(num_gen, max_pop_fit)
        plt.plot(num_gen, max_for_gen)
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.title('Fitness of Best Solution in Each Generation')
        return fig
       # plt.show()

