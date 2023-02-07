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
        while not os.path.exists("body"+str(solutionID)+".urdf"):
            time.sleep(0.05) 
        self.robot = ROBOT(solutionID)   
        self.world = WORLD(self.physicsClient, solutionID)
        pyrosim.Prepare_To_Simulate(self.robot.RobotId)
        
        self.topX = 10
        self.topY = -10
        self.topZ = -10


    def Run(self):
        for i in range(c.steps):
            if self.directOrGUI == "GUI":
                time.sleep(c.time_sleep)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            self.xPosBall = self.world.xPosBall()
            self.topX = min(self.xPosBall, self.topX)
            self.yPosBall = self.world.yPosBall()
            self.topY = max(self.yPosBall, self.topY)
            self.zPosBall = self.world.zPosBall()
            self.topZ = max(self.zPosBall, self.topZ)
        #return(self.topX, self.topY, self.topZ)


    def Get_Fitness(self):
        self.robot.Get_Fitness(self.topX,self.topY,self.topZ)

    def __del__(self):

        p.disconnect()