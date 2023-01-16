import pybullet_data
import pybullet as p
import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import time as time
import constants as c
from simulation import SIMULATION 

simulation = SIMULATION()
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,c.gravity)
# planeId = p.loadURDF("plane.urdf")
# RobotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(RobotId)
# backLegSensorValues = np.zeros(c.steps)
# frontLegSensorValues = np.zeros(c.steps)
# #targetAngles = np.sin(np.linspace(0, 2*np.pi, 1000))*(np.pi/4)
# BLtargetAngles = np.linspace(0, c.target_angles, c.steps)
# BLtargetAngles = c.BLamplitude*np.sin(c.BLfrequency*BLtargetAngles+c.BLphaseOffset)
# FLtargetAngles = np.linspace(0, c.target_angles, c.steps)
# FLtargetAngles = c.FLamplitude*np.sin(c.FLfrequency*FLtargetAngles+c.FLphaseOffset)
# #np.save(file = "data/sinus.npy", arr = BLtargetAngles)
# #np.save(file = "data/sinusfront.npy", arr = FLtargetAngles)
# #exit()
# for i in range(c.steps):
#     #print(i)
    
#     time.sleep(c.time_sleep)
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")    
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
#     #print(backLegSensorValues)
    
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = RobotId,
#         jointName = b'Torso_Backleg', 
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = BLtargetAngles[i],
#         maxForce = c.BLmaxForce)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = RobotId,
#         jointName = b'Torso_Frontleg', 
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = FLtargetAngles[i],
#         maxForce = c.FLmaxForce)
#     np.save(file = "data/sensordata.npy", arr = backLegSensorValues)
#     np.save(file = "data/sensordatafront.npy", arr = frontLegSensorValues)
# p.disconnect()
