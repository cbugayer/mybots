import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c

class WORLD:

    def __init__(self):
    
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
