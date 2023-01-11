import pybullet as p
import time as time
physicsClient = p.connect(p.GUI)
for i in range(1000):
    print(i)
    time.sleep(i)
    p.stepSimulation()
p.disconnect()