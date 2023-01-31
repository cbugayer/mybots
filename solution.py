import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:

    def __init__(self, AvailableID):

        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.length = 1
        self.width = 1
        self.height = 1
        self.x = 0
        self.y = 0 
        self.z = .5  

        self.myID = AvailableID
    
    # def Evaluate(self, directOrGUI):
    #     # print("FJN J NFOK FNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
    #     # print("start /B python3 simulate.py " + directOrGUI +" " + str(self.myID))
        
    #     self.Create_World()
    #     self.Create_Body()
    #     self.Create_Brain()
    #     s = str(self.myID)
    #     os.system("start /B "" python simulate.py " + directOrGUI +" " + s)
    #     #simulate.fun_s()
    #     #pyrosim.End()
    #     filename = "fitness" + str(self.myID) + ".txt"
    #     f = open(filename, "r")
    #     while not os.path.exists(filename):
    #         time.sleep(0.05)
    #     self.fitness = float(f.read())
    #     print(self.fitness)
    #     f.close()
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[self.x-3,self.y+3,self.z] , size=[self.length, self.width, self.height])
        pyrosim.End()
        
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[self.x,self.y,self.z+1] , size=[self.length, self.width, self.height])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [-.5,0,1])
        pyrosim.Send_Cube(name="Backleg", pos=[self.x-.5,self.y,self.z-1] , size=[self.length, self.width, self.height])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [.5,0,1])
        pyrosim.Send_Cube(name="Frontleg", pos=[self.x+.5,self.y,self.z-1] , size=[self.length, self.width, self.height])
        pyrosim.End()

    def Create_Brain(self):
        s = str(self.myID)
        f = open("brain" + s + ".nndf", "w")
        f.close()
        pyrosim.Start_NeuralNetwork("brain" + s + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        #print(self.weights)
        randRow = random.randint(0,2)
        randColumn = random.randint(0,1)
        self.weights[randRow][randColumn] = random.random() * 2 - 1
        #print(self.weights)

    def Set_ID(self, id):
        
        self.myID = id
    
    def Start_Simulation(self, directOrGUI):
        while not os.path.exists("world.sdf"):
            time.sleep(0.01)
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
        self.Create_World()
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