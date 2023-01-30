import numpy
import pyrosim.pyrosim as pyrosim
import simulate
import os
import random

class SOLUTION:

    def __init__(self):

        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.length = 1
        self.width = 1
        self.height = 1
        self.x = 0
        self.y = 0 
        self.z = .5  
    
    def Evaluate(self, directOrGUI):
        os.system("python simulate.py "+directOrGUI) 
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        #simulate.fun_s()
        #pyrosim.End()
        
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()
        
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
        pyrosim.Start_NeuralNetwork("brain.nndf")
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