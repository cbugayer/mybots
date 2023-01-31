import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from world import WORLD
from robot import ROBOT
import time
import os

class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if self.directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        #self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity) 
        while not os.path.exists("body.urdf"):
            time.sleep(0.05) 
        self.robot = ROBOT(solutionID)   
        self.world = WORLD(self.physicsClient)
        pyrosim.Prepare_To_Simulate(self.robot.RobotId)
        

    def Run(self):
        for i in range(c.steps):
            if self.directOrGUI == "GUI":
                time.sleep(c.time_sleep)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):

        p.disconnect()