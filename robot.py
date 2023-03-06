import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time
from pathlib import Path

class ROBOT:

    def __init__(self, solutionID):
        
        self.solutionID = solutionID
        # while not os.path.exists("brain"+str(self.solutionID)+".nndf"):
        #     time.sleep(1/100)
        myfile = Path("body"+str(self.solutionID)+".urdf")
        
        while not os.path.exists("body"+str(self.solutionID)+".urdf"):
            time.sleep(0.01)
        if myfile.is_file() and myfile.exists():
            self.RobotId = p.loadURDF("body"+str(self.solutionID)+".urdf")

        pyrosim.Prepare_To_Simulate(self.RobotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        os.system("del body"+str(self.solutionID)+".urdf")
        os.system("del brain"+str(self.solutionID)+".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for sensor_instance in self.sensors.values():
            sensor_instance.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        
    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName.encode('UTF-8')].Set_Value(self.RobotId, desiredAngle)
        
    def Think(self):
        self.nn.Update()
       # self.nn.Print()

    def Get_Fitness(self,topX,topY,topZ):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.RobotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        fitness = xPosition
        #f = open("fitness"+str(self.solutionID)+".txt", "w")
        f = open("tmp"+str(self.solutionID)+".txt", "w")
        
        #
        f.write(str(fitness))
        f.close()
        #os.system("rename tmp" + str(self.solutionID)+ ".txt" "fitness" + str(self.solutionID) + ".txt")
        os.rename("tmp" + str(self.solutionID)+ ".txt", "fitness" + str(self.solutionID) + ".txt")