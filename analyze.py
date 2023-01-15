import numpy as np
import matplotlib.pyplot as plt
backLegSensorValues = np.load("data/sensordata.npy")
frontLegSensorValues = np.load("data/sensordatafront.npy")
#print(backLegSensorValues)
plt.plot(backLegSensorValues, label = "Back", linewidth = 3)
plt.plot(frontLegSensorValues, label= "Front")
plt.legend()
plt.show()