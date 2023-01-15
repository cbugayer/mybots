import pybullet_data
import pybullet as p
import numpy as np
import pyrosim.pyrosim as pyrosim

import time as time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
RobotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(RobotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)
for i in range(1000):
    #print(i)
    time.sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")    
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    #print(backLegSensorValues)
    np.save(file = "data/sensordata.npy", arr = backLegSensorValues)
    np.save(file = "data/sensordatafront.npy", arr = frontLegSensorValues)
p.disconnect()
