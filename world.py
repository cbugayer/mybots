import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from pathlib import Path
import os
import time

class WORLD:

    def __init__(self, physicsClient, solutionID):
        
        self.myID = solutionID
        self.planeId = p.loadURDF("plane.urdf")
        myfile = Path("world" + str(self.myID) + ".sdf")
        while not os.path.exists("world" + str(self.myID) + ".sdf"):
            time.sleep(0.01)
        if myfile.is_file() and myfile.exists():
            self.objects = p.loadSDF("world" + str(self.myID) + ".sdf")
        os.system("del world"+str(self.myID)+".sdf")

    def xPosBall(self):
        
        posAndOrientation = p.getBasePositionAndOrientation(self.objects[0])

        position = posAndOrientation[0]

        xPosition = position[0]

        return(xPosition)

    def yPosBall(self):
        
        posAndOrientation = p.getBasePositionAndOrientation(self.objects[0])

        position = posAndOrientation[0]

        yPosition = position[1]

        return(yPosition)

    def zPosBall(self):
        
        posAndOrientation = p.getBasePositionAndOrientation(self.objects[0])

        position = posAndOrientation[0]

        zPosition = position[2]

        return(zPosition)
