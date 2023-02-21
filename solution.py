import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, AvailableID):
        
        self.num_links = random.randint(3,10)
        self.num_linksX = self.num_links
        self.numJoints = (self.num_links - 1)*self.num_linksX+self.num_links*(self.num_linksX-1)
        self.rand_links = []
        for _ in range(0, random.randint(1,self.num_links**2)):
            self.rand_links.append((random.randint(0,self.num_links),random.randint(0,self.num_links)))
        self.weights = numpy.random.rand(len(self.rand_links), self.numJoints)
        self.weights = self.weights * 2 - 1
        self.Ys = {}
        self.Xs = {}
        
        self.myID = AvailableID
        
    def Create_World(self):
        s = str(self.myID)
        f = open("world" + s + ".sdf", "w")
        f.close()
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.Send_Sphere(name="Ball", pos=[-1,1,2.5], size=[0.5], mass=0.1)
        # pyrosim.Send_Cube(name="Pole", pos=[-1,1,1] , size=[0.2,0.2,2], mass=100)
        # pyrosim.Send_Cube(name="Support1", pos=[-1.1,0.8,0.25] , size=[0.4,0.2,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support2", pos=[-1.2,1.1,0.25] , size=[0.2,0.4,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support3", pos=[-0.9,1.2,0.25] , size=[0.4,0.2,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support4", pos=[-0.8,0.9,0.25] , size=[0.2,0.4,0.5], mass=100)
        pyrosim.End()
        
    def Create_Random_Ys(self):
        
        for i in range(self.num_linksX):
            for j in range(self.num_links):
                if i != j:
                    self.Ys[(i,j)] = random.random()  
                else:
                    self.Ys[(i,j)] = 1

    def Create_Random_Xs(self):
        
        for i in range(self.num_linksX):
            for j in range(self.num_links):
                if i != j:
                    self.Xs[(i,j)] = random.random()  
                else:
                    self.Xs[(i,j)] = 1



    def Create_Body(self):
        s = str(self.myID)
        f = open("body" + s + ".urdf", "w")
        f.close()
        # print(self.Xs[(0,0)])
        # print(self.Ys[(0,0)])
        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        pyrosim.Send_Cube(name="Link(0,0)", pos=[0,0,0.5] , size=[self.Xs[(0,0)],self.Ys[(0,0)],1])
        pyrosim.Send_Joint( name = "Link(0,0)_Link(0,1)", parent= "Link(0,0)" , child = "Link(0,1)", type = "revolute", position = [0,self.Ys[(0,0)]/2,0.5], jointAxis = "0 0 1")
        pyrosim.Send_Joint( name = "Link(0,0)_Link(1,0)", parent= "Link(0,0)" , child = "Link(1,0)", type = "revolute", position = [self.Xs[(0,0)]/2,0,0.5], jointAxis = "0 0 1")
        pyrosim.Send_Joint( name = "Link(0,0)_Link(1,1)", parent= "Link(0,0)" , child = "Link(1,1)", type = "revolute", position = [self.Xs[(0,0)]/2,self.Ys[(0,0)]/2,0.5], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name = "Link(1,1)", pos = [self.Xs[(1,1)]/2,self.Ys[(1,1)]/2,0], size = [self.Xs[(1,1)],self.Ys[(1,1)],1])                  
        for i in range(1, self.num_linksX-1):
            pyrosim.Send_Joint( name = "Link(" + str(i) + ",0)_Link(" + str(i+1) + ",0)", parent= "Link(" + str(i) + ",0)" , child = "Link(" + str(i+1) + ",0)", type = "revolute", position = [self.Xs[(i,0)],0,0], jointAxis = "0 0 1")

        for j in range(1, self.num_links-1):
            pyrosim.Send_Joint( name = "Link(0," + str(j) + ")_Link(0," + str(j+1) + ")", parent= "Link(0," + str(j) + ")" , child = "Link(0," + str(j+1) + ")", type = "revolute", position = [0,self.Ys[(0,j)],0], jointAxis = "0 0 1")

        for i in range(1, self.num_linksX):
            pyrosim.Send_Cube(name="Link(" + str(i) + ",0)", pos=[self.Xs[(i,0)]/2,0,0] , size=[self.Xs[(i,0)],self.Ys[(i,0)],1])

        for j in range(1, self.num_links):
            pyrosim.Send_Cube(name="Link(0," + str(j) + ")", pos=[0,self.Ys[(0,j)]/2,0] , size=[self.Xs[(0,j)],self.Ys[(0,j)],1])

        for i in range(1, self.num_linksX - 1):
            pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(i) + ")_Link(" + str(i+1) + "," + str(i+1) + ")", parent= "Link(" + str(i) + "," + str(i) + ")" , child = "Link(" + str(i+1) + "," + str(i+1) + ")", type = "revolute", position = [self.Xs[(i,i)],self.Ys[(i,i)],0], jointAxis = "0 0 1")
            pyrosim.Send_Cube(name="Link(" + str(i+1) + "," + str(i+1) + ")", pos=[self.Xs[(i+1,i+1)]/2,self.Ys[(i+1,i+1)]/2,0] , size=[self.Xs[(i+1,i+1)],self.Ys[(i+1,i+1)],1])

            pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(i) + ")_Link(" + str(i+1) + "," + str(i) + ")", parent= "Link(" + str(i) + "," + str(i) + ")" , child = "Link(" + str(i+1) + "," + str(i) + ")", type = "revolute", position = [self.Xs[(i,i)],self.Ys[(i,i)]/2,0], jointAxis = "0 0 1")
            pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(i) + ")_Link(" + str(i) + "," + str(i+1) + ")", parent= "Link(" + str(i) + "," + str(i) + ")" , child = "Link(" + str(i) + "," + str(i+1) + ")", type = "revolute", position = [self.Xs[(i,i)]/2,self.Ys[(i,i)],0], jointAxis = "0 0 1")

            pyrosim.Send_Cube(name="Link(" + str(i+1) + "," + str(i) + ")", pos=[self.Xs[(i+1,i)]/2,0,0] , size=[self.Xs[(i+1,i)],self.Ys[(i+1,i)],1])
            pyrosim.Send_Cube(name="Link(" + str(i) + "," + str(i+1) + ")", pos=[0,self.Ys[(i,i+1)]/2,0] , size=[self.Xs[(i,i+1)],self.Ys[(i,i+1)],1])

            for x in range(i+1, self.num_linksX-1):
                pyrosim.Send_Joint( name = "Link(" + str(x) + "," + str(i) + ")_Link(" + str(x+1) + "," + str(i) + ")", parent= "Link(" + str(x) + "," + str(i) + ")" , child = "Link(" + str(x+1) + "," + str(i) + ")", type = "revolute", position = [self.Xs[(x,i)],0,0], jointAxis = "0 0 1")
                pyrosim.Send_Cube(name="Link(" + str(x+1) + "," + str(i) + ")", pos=[self.Xs[(x+1,i)]/2,0,0] , size=[self.Xs[(x+1,i)],self.Ys[(x+1,i)],1])
            for y in range(i+1, self.num_links-1):
                pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(y) + ")_Link(" + str(i) + "," + str(y+1) + ")", parent= "Link(" + str(i) + "," + str(y) + ")" , child = "Link(" + str(i) + "," + str(y+1) + ")", type = "revolute", position = [0,self.Ys[(i,y)],0], jointAxis = "0 0 1")
                pyrosim.Send_Cube(name="Link(" + str(i) + "," + str(y+1) + ")", pos=[0,self.Ys[(i,y+1)]/2,0] , size=[self.Xs[(i,y+1)],self.Ys[(i,y+1)],1])


        # pyrosim.Send_Joint( name = "Link(0,0)_Link(0,1)", parent= "Link(0,0)" , child = "Link(0,1)", type = "revolute", position = [0,1/2,0.5], jointAxis = "0 0 1")
        # pyrosim.Send_Joint( name = "Link(0,0)_Link(1,0)", parent= "Link(0,0)" , child = "Link(1,0)", type = "revolute", position = [1/2,0,0.5], jointAxis = "0 0 1")
        # pyrosim.Send_Cube(name="Link(0,1)", pos=[0,1/2,0] , size=[1,1,1])
        # pyrosim.Send_Cube(name="Link(1,0)", pos=[1/2,0,0] , size=[1,1,1])

        # pyrosim.Send_Joint( name = "Link(1,0)_Link(2,0)", parent= "Link(1,0)" , child = "Link(2,0)", type = "revolute", position = [1,0,0], jointAxis = "0 0 1")
        # pyrosim.Send_Joint( name = "Link(0,1)_Link(0,2)", parent= "Link(0,1)" , child = "Link(0,2)", type = "revolute", position = [0,1,0], jointAxis = "0 0 1")
        # # pyrosim.Send_Joint( name = "Link(0,1)_Link(1,1)", parent= "Link(0,1)" , child = "Link(1,1)", type = "revolute", position = [1/2,1/2,0], jointAxis = "0 0 1")
        # # pyrosim.Send_Joint( name = "Link(1,0)_Link(1,1)", parent= "Link(1,0)" , child = "Link(1,1)", type = "revolute", position = [1/2,1/2,0], jointAxis = "0 0 1")

        # # pyrosim.Send_Cube(name="Link(1,1)", pos=[1/2,1/2,0] , size=[1,1,1])
        # pyrosim.Send_Cube(name="Link(2,0)", pos=[1/2,0,0] , size=[1,1,1])
        # pyrosim.Send_Cube(name="Link(0,2)", pos=[0,1/2,0] , size=[1,1,1])

       
       
       
       
        # pyrosim.Send_Cube(name="Link(1,0)", pos=[1/2,0,0] , size=[1,1,1])   
        # pyrosim.Send_Cube(name="Link(0,1)", pos=[0,1/2,0] , size=[1,1,1])
        # pyrosim.Send_Joint( name = "Link(1,0)_Link(1,1)", parent= "Link(1,0)" , child = "Link(1,1)", type = "revolute", position = [1/2,1/2,0], jointAxis = "0 0 1")
        # pyrosim.Send_Joint( name = "Link(1,0)_Link(2,0)", parent= "Link(1,0)" , child = "Link(2,0)", type = "revolute", position = [1,0,0], jointAxis = "0 0 1")
        # pyrosim.Send_Cube(name="Link(2,0)", pos=[1/2,0,0] , size=[1,1,1])
        # pyrosim.Send_Cube(name="Link(1,1)", pos=[0,1/2,0] , size=[1,1,1])
        # # Because i = 3 - 1, we only need one joint and one cube
        # pyrosim.Send_Joint( name = "Link(2,0)_Link(2,1)", parent= "Link(2,0)" , child = "Link(2,1)", type = "revolute", position = [1/2,1/2,0], jointAxis = "0 0 1")
        # pyrosim.Send_Cube(name="Link(2,1)", pos=[0,1/2,0] , size=[1,1,1])
        # # pyrosim.Send_Joint( name = "Link(2,1)_Link(2,2)", parent= "Link(2,1)" , child = "Link(3,0)", type = "revolute", position = [0,1,0], jointAxis = "0 0 1")
        # # pyrosim.Send_Joint( name = "Link(2,1)_Link(1,1)", parent= "Link(2,1)" , child = "Link(1,1)", type = "revolute", position = [-1/2,1/2,0], jointAxis = "0 0 1")
        # # pyrosim.Send_Cube(name="Link(2,2)", pos=[0,1/2,0] , size=[1,1,1])        
        # # pyrosim.Send_Joint( name = "Link(2,1)_Link(1,1)", parent= "Link(2,1)" , child = "Link(1,1)", type = "revolute", position = [-1/2,1/2,0], jointAxis = "0 0 1")
                           

       
        # pyrosim.Send_Cube(name="Link(0,0)", pos=[0,0,0.5] , size=[self.Xs[(0,0)],self.Ys[(0,0)],random.random()])
        # pyrosim.Send_Joint( name = "Link(0,0)_Link(0,1)", parent= "Link(0,0)" , child = "Link(0,1)", type = "revolute", position = [0,self.Ys[(0,0)]/2,0.5], jointAxis = "0 0 1")
        # pyrosim.Send_Cube(name="Link(0,1)", pos=[0,self.Ys[(0,0)]/2,0] , size=[self.Xs[(0,1)],self.Ys[(0,1)],random.random()])
        # pyrosim.Send_Joint( name = "Link(0,0)_Link(1,0)", parent= "Link(0,0)" , child = "Link(1,0)", type = "revolute", position = [self.Xs[(0,0)]/2,-self.Ys[(0,0)]/2,0], jointAxis = "0 0 1")
        # pyrosim.Send_Cube(name="Link(1,0)", pos=[self.Xs[(0,0)]/2,0,0] , size=[self.Xs[(1,0)],self.Ys[(1,0)],random.random()])
        
        
        # for j in range(0,self.num_links):
        #     if j == 0 or j % 2 == 0:
        #         if j != 0:
        #             if (0,j) in self.rand_links:
        #                 pyrosim.Send_Cube(name="Link(0,"+str(j)+")", pos=[0,self.Ys[(0,j)]/2,0] , size=[self.Xs[(0,j)],self.Ys[(0,j)],random.random()], color = "green")
        #             else:
        #                 pyrosim.Send_Cube(name="Link(0,"+str(j)+")", pos=[0,self.Ys[(0,j)]/2,0] , size=[self.Xs[(0,j)],self.Ys[(0,j)],random.random()])
        #             if j != self.num_links - 1:
        #                 pyrosim.Send_Joint( name = "Link(0,"+str(j)+")_Link(0,"+str(j+1)+")" , parent= "Link(0,"+str(j)+")" , child = "Link(0,"+str(j+1)+")" , type = "revolute", position = [0,self.Ys[(0,j)],0], jointAxis = "0 0 1")
        #                 pyrosim.Send_Joint( name = "Link(0,"+str(j)+")_Link(1,"+str(j)+")" , parent= "Link(0,"+str(j)+")" , child = "Link(1,"+str(j)+")" , type = "revolute", position = [self.Xs[(0,j)]/2,-self.Ys[(0,j)]/2,0], jointAxis = "0 0 1")
        #             else:
        #                 pyrosim.Send_Joint( name = "Link(0,"+str(j)+")_Link(1,"+str(j)+")" , parent= "Link(0,"+str(j)+")" , child = "Link(1,"+str(j)+")" , type = "revolute", position = [self.Xs[(0,j)]/2,self.Ys[(0,j)]/2,0], jointAxis = "0 0 1")
        #         for i in range(1, self.num_linksX):
        #             if (i,j) in self.rand_links:
        #                 pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()], color = "green")
        #             else:
        #                 pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()])
        #             if j != self.num_links - 1:
        #                 pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i,j+1)) , parent= "Link"+str((i,j)) , child = "Link"+str((i,j+1)) , type = "revolute", position = [self.Xs[(i,j)]/2,self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
        #                 if i != self.num_linksX - 1:
        #                     pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i+1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i+1,j)) , type = "revolute", position = [self.Xs[(i,j)]/2,-self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
        #             else:
        #                 if i != self.num_linksX - 1:
        #                     pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i+1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i+1,j)) , type = "revolute", position = [self.Xs[(i,j)],0,0], jointAxis = "0 0 1")
        #     else:
        #         if (self.num_linksX - 1,j) in self.rand_links:
        #             pyrosim.Send_Cube(name="Link"+str((self.num_linksX - 1, j)), pos=[0,self.Ys[(self.num_linksX - 1,j)]/2,0] , size=[self.Xs[(self.num_linksX - 1,j)],self.Ys[(self.num_linksX - 1,j)],random.random()], color = "green")
        #         else:
        #             pyrosim.Send_Cube(name="Link"+str((self.num_linksX - 1, j)), pos=[0,self.Ys[(self.num_linksX - 1,j)]/2,0] , size=[self.Xs[(self.num_linksX - 1,j)],self.Ys[(self.num_linksX - 1,j)],random.random()])
        #         if j != self.num_links - 1:
        #             pyrosim.Send_Joint( name = "Link"+str((self.num_linksX - 1, j))+"_Link"+str((self.num_linksX - 1, j+1)) , parent= "Link"+str((self.num_linksX - 1, j)) , child = "Link"+str((self.num_linksX - 1, j+1)) , type = "revolute", position = [0,self.Ys[(self.num_linksX - 1,j)],0], jointAxis = "0 0 1")
        #             pyrosim.Send_Joint( name = "Link"+str((self.num_linksX - 1, j))+"_Link"+str((self.num_linksX - 2, j)) , parent= "Link"+str((self.num_linksX - 1, j)) , child = "Link"+str((self.num_linksX - 2, j)) , type = "revolute", position = [-self.Xs[(self.num_linksX - 1,j)]/2,-self.Ys[(self.num_linksX - 1,j)]/2,0], jointAxis = "0 0 1")
        #         else:
        #             pyrosim.Send_Joint( name = "Link"+str((self.num_linksX - 1, j))+"_Link"+str((self.num_linksX - 2, j)) , parent= "Link"+str((self.num_linksX - 1, j)) , child = "Link"+str((self.num_linksX - 2, j)) , type = "revolute", position = [-self.Xs[(self.num_linksX - 1,j)]/2,self.Ys[(self.num_linksX - 1,j)]/2,0], jointAxis = "0 0 1")
        #         for i in range(self.num_linksX - 2, -1, -1):
        #             if (i,j) in self.rand_links:
        #                 pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[-self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()], color = "green")
        #             else:
        #                 pyrosim.Send_Cube(name="Link"+str((i,j)), pos=[-self.Xs[(i,j)]/2,0,0] , size=[self.Xs[(i,j)],self.Ys[(i,j)],random.random()])
        #             if j != self.num_links - 1:
        #                 pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i,j+1)) , parent= "Link"+str((i,j)) , child = "Link"+str((i,j+1)) , type = "revolute", position = [-self.Xs[(i,j)]/2,self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
        #                 if i != 0:
        #                     pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i-1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i-1,j)) , type = "revolute", position = [-self.Xs[(i,j)]/2,-self.Ys[(i,j)]/2,0], jointAxis = "0 0 1")
        #             else:
        #                 if i != 0:
        #                     pyrosim.Send_Joint( name = "Link"+str((i,j))+"_Link"+str((i+1,j)) , parent= "Link"+str((i,j)) , child = "Link"+str((i+1,j)) , type = "revolute", position = [-self.Xs[(i,j)],0,0], jointAxis = "0 0 1")

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
        
        # for j in range(self.num_links):    
        #     for i in range(self.num_linksX - 1):
        #         pyrosim.Send_Motor_Neuron(name = i + j*self.num_linksX , jointName = "Link"+str((i,j))+"_Link"+str((i+1,j)))
        
        # for j in range(self.num_links - 1):
        #     for i in range(self.num_linksX):
        #         pyrosim.Send_Motor_Neuron(name = i + j*self.num_linksX + self.num_links*(self.num_linksX - 1) , jointName = "Link"+str((i,j))+"_Link"+str((i+1,j)))
        # for ind, rand_tup in enumerate(self.rand_links):
        #     pyrosim.Send_Sensor_Neuron(name =  self.numJoints + ind, linkName = "Link"+str(rand_tup))
        
        # for currentRow in range(len(self.rand_links)):
        #     for ccj in range(self.num_links):
        #         for cci in range(self.num_linksX):
        #             pyrosim.Send_Synapse( sourceNeuronName = currentRow + self.numJoints, targetNeuronName = cci + ccj*self.num_linksX, weight = self.weights[currentRow][cci][ccj] )
        pyrosim.End()

    def Mutate(self):
        #print(self.weights)
        randRow = random.randint(0,len(self.rand_links) - 1)
        randColumn = random.randint(0,self.numJoints- 1)
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