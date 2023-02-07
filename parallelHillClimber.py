from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del world*.sdf")
        os.system("del body*.urdf")
        self.parents = {}
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
            if self.parents[p].fitness < self.children[p].fitness:
                self.parents[p] = self.children[p]

    def Print(self):
        print("\n")
        for p in self.parents.keys():
            print(self.parents[p], self.children[p])
        print("\n")

    def Show_Best(self):
        fit = {}
        for p in self.parents.values():
            fit[p] = p.fitness
        print(fit)
        top = max(fit, key=fit.get)
        print(top.fitness)
        top.Start_Simulation("GUI")
        

    def Evaluate(self,solutions):
        for pc in solutions.values():
            pc.Start_Simulation("DIRECT")
        for pc in solutions.values():
            pc.Wait_For_Simulation_To_End()
