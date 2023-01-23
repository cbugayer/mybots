import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:

    def __init__(self):
        
        self.RobotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.RobotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")

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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                print(self.motors)
                self.motors[jointName.encode('UTF-8')].Set_Value(self.RobotId, desiredAngle)
                # ind = pyrosim.jointNamesToIndices[jointName]
                # self.motors[ind].Set_Value(self.RobotId, desiredAngle)
        
    def Think(self):
        self.nn.Update()
        self.nn.Print()