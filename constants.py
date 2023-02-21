import numpy as np
steps = 1000

gravity = -9.8
BLamplitude = np.pi/2
BLfrequency = 10
BLphaseOffset = np.pi/4

BLmaxForce = 40

FLamplitude = np.pi/2
FLfrequency = 1000
FLphaseOffset = np.pi

FLmaxForce = 40

target_angles = 2*np.pi

time_sleep = 1/60

numberOfGenerations = 1

populationSize = 1

numSensorNeurons = 9

numMotorNeurons = 8

motorJointRange = 0.2