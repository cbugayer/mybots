import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim

import time as time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
RobotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(RobotId)
for i in range(1000):
    #print(i)
    time.sleep(1/60)
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")    
    print(backLegTouch)
p.disconnect()