import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, AvailableID):
        
        self.num_links = random.randint(2,40)
        self.num_linksX = random.randint(2,40)
        self.rand_links = []
        for _ in range(0, random.randint(1,self.num_links * self.num_linksX)):
            self.rand_links.append((random.randint(0,self.num_linksX),random.randint(0,self.num_links)))
        self.weights = numpy.random.rand(self.num_links - 1,self.num_links - 1)
        self.weights = self.weights * 2 - 1
        self.Ys = {}
        self.Xs = {}
        
        self.myID = AvailableID
        
    def Create_World(self):
        s = str(self.myID)
        f = open("world" + s + ".sdf", "w")
        f.close()
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        # pyrosim.Send_Sphere(name="Ball", pos=[-1,1,2.5], size=[0.5], mass=0.1)
        # pyrosim.Send_Cube(name="Pole", pos=[-1,1,1] , size=[0.2,0.2,2], mass=100)
        # pyrosim.Send_Cube(name="Support1", pos=[-1.1,0.8,0.25] , size=[0.4,0.2,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support2", pos=[-1.2,1.1,0.25] , size=[0.2,0.4,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support3", pos=[-0.9,1.2,0.25] , size=[0.4,0.2,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support4", pos=[-0.8,0.9,0.25] , size=[0.2,0.4,0.5], mass=100)
        pyrosim.End()
        
    def Create_Random_Ys(self):
        
        for i in range(self.num_linksX):
            for j in range(self.num_links):
                self.Ys[(i, j)] = random.random()

    def Create_Random_Xs(self):
        
        for i in range(self.num_linksX):
            for j in range(self.num_links):
                self.Xs[(i,j)] = random.random()    


    def Create_Body(self):
        s = str(self.myID)
        f = open("body" + s + ".urdf", "w")
        f.close()
        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        pyrosim.Send_Cube(name="Link(0,0)", pos=[0,0,0.5] , size=[self.Xs[(0,0)],self.Ys[(0,0)],random.random()])
        pyrosim.Send_Joint( name = "Link(0,0)_Link(0,1)", parent= "Link(0,0)" , child = "Link(0,1)", type = "revolute", position = [0,self.Ys[(0,0)]/2,0.5], jointAxis = "0 0 1")
        pyrosim.Send_Joint( name = "Link(0,0)_Link(1,0)", parent= "Link(0,0)" , child = "Link(1,0)", type = "revolute", position = [self.Xs[(0,0)]/2,-self.Ys[(0,0)]/2,0], jointAxis = "0 0 1")
        for j in range(0,self.num_links):
            if j % 2 == 0:
                if j != 0:
                    if (0,j) in self.rand_links:
                        pyrosim.Send_Cube(name="Link(0,"+str(j)+")", pos=[0,self.Ys[(0,j)]/2,0] , size=[self.Xs[(0,j)],self.Ys[(0,j)],random.random()], color = "green")
                    else:
                        pyrosim.Send_Cube(name="Link(0,"+str(j)+")", pos=[0,self.Ys[(0,j)]/2,0] , size=[self.Xs[(0,j)],self.Ys[(0,j)],random.random()])
                    if j != self.num_links - 1:
                        pyrosim.Send_Joint( name = "Link(0,"+str(j)+")_Link(0,"+str(j+1)+")" , parent= "Link(0,"+str(j)+")" , child = "Link(0,"+str(j+1)+")" , type = "revolute", position = [0,self.Ys[(0,j)],0], jointAxis = "0 0 1")
                        pyrosim.Send_Joint( name = "Link(0,"+str(j)+")_Link(1,"+str(j)+")" , parent= "Link(0,"+str(j)+")" , child = "Link(1,"+str(j)+")" , type = "revolute", position = [self.Xs[(0,j)]/2,-self.Ys[(0,j)]/2,0], jointAxis = "0 0 1")
                    else:
                        pyrosim.Send_Joint( name = "Link(0,"+str(j)+")_Link(1,"+str(j)+")" , parent= "Link(0,"+str(j)+")" , child = "Link(1,"+str(j)+")" , type = "revolute", position = [self.Xs[(0,j)]/2,self.Ys[(0,j)]/2,0], jointAxis = "0 0 1")
                for i in range(1, self.num_linksX):
                    if (i,j) in self.rand_links:
                        pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()], color = "green")
                    else:
                        pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()])
                    if j != self.num_links - 1:
                        pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i,j+1)) , parent= "Link"+str((i,j)) , child = "Link"+str((i,j+1)) , type = "revolute", position = [self.Xs[(i,j)]/2,self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
                        if i != self.num_linksX - 1:
                            pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i+1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i+1,j)) , type = "revolute", position = [self.Xs[(i,j)]/2,-self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
                    else:
                        if i != self.num_linksX - 1:
                            pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i+1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i+1,j)) , type = "revolute", position = [self.Xs[(i,j)],0,0], jointAxis = "0 0 1")
            else:
                if (self.num_linksX - 1,j) in self.rand_links:
                    pyrosim.Send_Cube(name="Link"+str((self.num_linksX - 1, j)), pos=[0,self.Ys[(self.num_linksX - 1,j)]/2,0] , size=[self.Xs[(self.num_linksX - 1,j)],self.Ys[(self.num_linksX - 1,j)],random.random()], color = "green")
                else:
                    pyrosim.Send_Cube(name="Link"+str((self.num_linksX - 1, j)), pos=[0,self.Ys[(self.num_linksX - 1,j)]/2,0] , size=[self.Xs[(self.num_linksX - 1,j)],self.Ys[(self.num_linksX - 1,j)],random.random()])
                if j != self.num_links - 1:
                    pyrosim.Send_Joint( name = "Link"+str((self.num_linksX - 1, j))+"_Link"+str((self.num_linksX - 1, j+1)) , parent= "Link"+str((self.num_linksX - 1, j)) , child = "Link"+str((self.num_linksX - 1, j+1)) , type = "revolute", position = [0,self.Ys[(self.num_linksX - 1,j)],0], jointAxis = "0 0 1")
                    pyrosim.Send_Joint( name = "Link"+str((self.num_linksX - 1, j))+"_Link"+str((self.num_linksX - 2, j)) , parent= "Link"+str((self.num_linksX - 1, j)) , child = "Link"+str((self.num_linksX - 2, j)) , type = "revolute", position = [-self.Xs[(self.num_linksX - 1,j)]/2,-self.Ys[(self.num_linksX - 1,j)]/2,0], jointAxis = "0 0 1")
                else:
                    pyrosim.Send_Joint( name = "Link"+str((self.num_linksX - 1, j))+"_Link"+str((self.num_linksX - 2, j)) , parent= "Link"+str((self.num_linksX - 1, j)) , child = "Link"+str((self.num_linksX - 2, j)) , type = "revolute", position = [-self.Xs[(self.num_linksX - 1,j)]/2,self.Ys[(self.num_linksX - 1,j)]/2,0], jointAxis = "0 0 1")
                for i in range(self.num_linksX - 2, -1, -1):
                    if (i,j) in self.rand_links:
                        pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[-self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()], color = "green")
                    else:
                        pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[-self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()])
                    if j != self.num_links - 1:
                        pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i,j+1)) , parent= "Link"+str((i,j)) , child = "Link"+str((i,j+1)) , type = "revolute", position = [-self.Xs[(i,j)]/2,self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
                        if i != 0:
                            pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i-1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i-1,j)) , type = "revolute", position = [-self.Xs[(i,j)]/2,-self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
                    else:
                        if i != 0:
                            pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i+1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i+1,j)) , type = "revolute", position = [-self.Xs[(i,j)],0,0], jointAxis = "0 0 1")

        # count = 1
        # for i in range(self.num_linksX + self.num_links - 2, -1, self.num_links):
        #     pyrosim.Send_Cube(name="Link"+str(i), pos=[self.Xs[(i-count)],self.Ys[i-count],0] , size=[self.Xs[i-count]/2+self.Xs[i],self.Ys[i],random.random()])
        #     count += 1
            


        pyrosim.End()

    def Create_Brain(self):
        s = str(self.myID)
        f = open("brain" + s + ".nndf", "w")
        f.close()
        pyrosim.Start_NeuralNetwork("brain" + s + ".nndf")
        # for i in range(self.num_links - 1):
        #     pyrosim.Send_Motor_Neuron(name = i , jointName = "Link"+str(i)+"_Link"+str(i+1)) 
        # for ind, rand_num in enumerate(self.rand_links):
        #     pyrosim.Send_Sensor_Neuron(name =  self.num_links - 1 + ind, linkName = "Link"+str(rand_num))
        
        # for currentRow in range(len(self.rand_links)):
        #     for currentColumn in range(self.num_links - 1):
        #         pyrosim.Send_Synapse( sourceNeuronName = currentRow+self.num_links - 1  , targetNeuronName = currentColumn, weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        #print(self.weights)
        randRow = random.randint(0,c.numSensorNeurons - 1)
        randColumn = random.randint(0,c.numMotorNeurons - 1)
        self.weights[randRow][randColumn] = random.random() * 2 - 1
        #print(self.weights)

    def Set_ID(self, id):
        
        self.myID = id
    
    def Start_Simulation(self, directOrGUI):
        # while not os.path.exists("world" + str(self.myID) + ".sdf"):
        #     time.sleep(0.01)
        # while not os.path.exists("body.urdf"):
        #     time.sleep(0.01)
        self.Create_World()
        self.Create_Random_Ys()
        self.Create_Random_Xs()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGUI +" " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        filename = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(filename):
            time.sleep(0.01)
        assert os.path.isfile(filename)
        f = open(filename, "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()
        os.system("del fitness"+str(self.myID)+".txt")