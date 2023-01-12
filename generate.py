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
    
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z+1] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-.5,1])
    pyrosim.Send_Cube(name="Backleg", pos=[x,y-.5,z-1] , size=[length, width, height])
    pyrosim.Send_Joint( name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0,-.5,1])
    pyrosim.Send_Cube(name="Frontleg", pos=[x,y+1.5,z-1] , size=[length, width, height])
    pyrosim.End()
Create_Robot()
Create_World()
