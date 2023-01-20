import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.BLamplitude
        self.frequency = c.BLfrequency
        self.offset = c.BLphaseOffset

        if self.jointName.decode() == "Torso_Backleg":
            self.frequency = self.frequency / 100
        targetAngles = np.linspace(0, c.target_angles, c.steps)
        self.motorValues = self.amplitude*np.sin(self.frequency*targetAngles+self.offset)
         
    def Set_Value(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot,
                jointName = self.jointName, 
                controlMode = p.POSITION_CONTROL,
                targetPosition = desiredAngle,
                maxForce = c.BLmaxForce)
    
    def Save_Values(self):
        np.save(file = "data/moto_dat.npy", arr = self.motorValues)
