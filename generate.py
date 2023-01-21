import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0 
z = .5
#for a in range(5):
#    for b in range(5):
#        for i in range(10): 
#            pyrosim.Send_Cube(name="Box", pos=[x+a,y+b,z+i] , size=[length * (.9 ** i), width * (.9 ** i), height * (.9 ** i)])
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x-3,y+3,z] , size=[length, width, height])
    pyrosim.End()
    
def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z+1] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [-.5,0,1])
    pyrosim.Send_Cube(name="Backleg", pos=[x-.5,y,z-1] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [.5,0,1])
    pyrosim.Send_Cube(name="Frontleg", pos=[x+.5,y,z-1] , size=[length, width, height])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Backleg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "Frontleg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_Backleg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_Frontleg")
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
    pyrosim.End()

def Create_Robot():
    pass
Generate_Body()
Generate_Brain()
Create_Robot()
Create_World()
