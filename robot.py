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
        
    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                for motor_instance in self.motors.values():
                    motor_instance.Set_Value(self.RobotId, desiredAngle)
                print(neuronName, jointName, desiredAngle)
        # for motor_instance in self.motors.values():
        #     motor_instance.Set_Value(self.RobotId, t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()