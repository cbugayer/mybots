import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, AvailableID):

        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

        self.myID = AvailableID
        
    def Create_World(self):
        s = str(self.myID)
        f = open("world" + s + ".sdf", "w")
        f.close()
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.Send_Sphere(name="Ball", pos=[-1,1,2.5], size=[0.5], mass=0.1)
        pyrosim.Send_Cube(name="Pole", pos=[-1,1,1] , size=[0.2,0.2,2], mass=100)
        pyrosim.Send_Cube(name="Support1", pos=[-1.1,0.8,0.25] , size=[0.4,0.2,0.5], mass=100)
        pyrosim.Send_Cube(name="Support2", pos=[-1.2,1.1,0.25] , size=[0.2,0.4,0.5], mass=100)
        pyrosim.Send_Cube(name="Support3", pos=[-0.9,1.2,0.25] , size=[0.4,0.2,0.5], mass=100)
        pyrosim.Send_Cube(name="Support4", pos=[-0.8,0.9,0.25] , size=[0.2,0.4,0.5], mass=100)
        pyrosim.End()
        
    def Create_Body(self):
        s = str(self.myID)
        f = open("body" + s + ".urdf", "w")
        f.close()
        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Backleg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Frontleg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Rightleg", pos=[0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-0.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Leftleg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Frontleg_Frontlowerleg" , parent= "Frontleg" , child = "Frontlowerleg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Frontlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Backleg_Backlowerleg" , parent= "Backleg" , child = "Backlowerleg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Backlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Rightleg_Rightlowerleg" , parent= "Rightleg" , child = "Rightlowerleg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Rightlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Leftleg_Leftlowerleg" , parent= "Leftleg" , child = "Leftlowerleg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Leftlowerleg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "Torso_Body" , parent= "Torso" , child = "Body" , type = "revolute", position = [0,0,1.5], jointAxis = "0 0 1")
        pyrosim.Send_Cube(name="Body", pos=[0,0,0.5], size=[1,1,1])
        pyrosim.Send_Joint( name = "Body_Bat1" , parent= "Body" , child = "Bat1" , type = "revolute", position = [-0.5,0,0.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Bat1", pos=[-0.5,0,0] , size=[1,0.2,0.2], mass=10)
        pyrosim.Send_Joint( name = "Body_Bat2" , parent= "Body" , child = "Bat2" , type = "revolute", position = [0.5,0,0.5], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Bat2", pos=[0.5,0,0] , size=[1,0.2,0.2], mass=10)
        pyrosim.End()

    def Create_Brain(self):
        s = str(self.myID)
        f = open("brain" + s + ".nndf", "w")
        f.close()
        pyrosim.Start_NeuralNetwork("brain" + s + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "Rightleg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "Leftleg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "Backlowerleg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "Frontlowerleg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "Rightlowerleg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "Leftlowerleg")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "Body")
        pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "Bat1")
        pyrosim.Send_Sensor_Neuron(name = 11 , linkName = "Bat2")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_Backleg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_Frontleg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_Rightleg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_Leftleg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Backleg_Backlowerleg")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Frontleg_Frontlowerleg")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "Rightleg_Rightlowerleg")
        pyrosim.Send_Motor_Neuron( name = 19 , jointName = "Leftleg_Leftlowerleg")
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "Torso_Body")
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Body_Bat1")
        pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Body_Bat2")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn] )
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