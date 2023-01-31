import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from pathlib import Path
import os
import time

class WORLD:

    def __init__(self, physicsClient):
        
        self.planeId = p.loadURDF("plane.urdf")
        myfile = Path("world.sdf")
        while not os.path.exists("world.sdf"):
                time.sleep(0.01)
        if myfile.is_file() and myfile.exists():
            p.loadSDF("world.sdf")
