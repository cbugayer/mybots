import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:

    def __init__(self, AvailableID):
        
        self.num_links = random.randint(1,4)
        self.num_legs = random.randint(0,4)
        if self.num_legs == 0 and self.num_links == 1:
            self.num_legs = 1

        self.links = []
        for i in range(0, self.num_links):
            self.links.append("Body"+str(i))
            for j in range(0,self.num_legs):
                self.links.append("Leg"+str(i)+"right"+str(j))
                self.links.append("Leg"+str(i)+"left"+str(j))
        
        self.rand_links = [self.links[i] for i in random.sample(range(len(self.links)), random.randint(0, len(self.links) - 1))]
        
        #print(self.num_links)
        # self.numJoints = self.num_links**2 -1 + 9*self.num_links
        self.numJoints = self.num_links - 1 + self.num_legs*2*self.num_links

        # for _ in range(0, random.randint(1,self.num_links**2)):
        #     self.rand_links.append((random.randint(0,self.num_links-1),random.randint(0,self.num_links-1)))
        # for i in range(0, random.randint(1,self.num_links)):
        #     self.rand_links.append("Under"+str(i))
        #     for j in range(0,random.randint(0,4)):
        #         self.rand_links.append("Arm"+str(i)+str(j))
        #     for j in range(0,random.randint(0,4)):
        #         self.rand_links.append("Leg"+str(i)+str(j))
        
        print(self.links)
        self.weights = numpy.random.rand(len(self.rand_links), self.numJoints)
        self.weights = self.weights * 2 - 1

        self.fitness = 0

        self.Arms = numpy.random.rand(self.num_links*4) * .5
        self.Legs = numpy.random.rand(self.num_links*4) * 2
        # self.Ys = {}
        # self.Xs = {}
        # for i in range(self.num_links):
        #     for j in range(self.num_links):
        #         if i != j:
        #             self.Ys[(i,j)] = random.random()
        #         else:
        #             self.Ys[(i,j)] = 1

        # for i in range(self.num_links):
        #     for j in range(self.num_links):
        #         if i != j:
        #             self.Xs[(i,j)] = random.random()  
        #         else:
        #             self.Xs[(i,j)] = 1

        self.myID = AvailableID
        
    def Create_World(self):
        s = str(self.myID)
        f = open("world" + s + ".sdf", "w")
        f.close()
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.Send_Sphere(name="Ball", pos=[-1,1,1+max(self.Legs)], size=[0.5], mass=0.1)
        # pyrosim.Send_Cube(name="Pole", pos=[-1,1,1] , size=[0.2,0.2,2], mass=100)
        # pyrosim.Send_Cube(name="Support1", pos=[-1.1,0.8,0.25] , size=[0.4,0.2,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support2", pos=[-1.2,1.1,0.25] , size=[0.2,0.4,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support3", pos=[-0.9,1.2,0.25] , size=[0.4,0.2,0.5], mass=100)
        # pyrosim.Send_Cube(name="Support4", pos=[-0.8,0.9,0.25] , size=[0.2,0.4,0.5], mass=100)
        pyrosim.End()
        
    def Send_Cube(self, name, pos, size, mass):
        if name in self.rand_links:
            pyrosim.Send_Cube(name=name, pos=pos , size=size, mass=mass, color="green")
        else:
            pyrosim.Send_Cube(name=name, pos=pos , size=size, mass=mass)


    def Create_Body(self):
        s = str(self.myID)
        f = open("body" + s + ".urdf", "w")
        f.close()

        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        x = random.random() * 3
        y = random.random() * 3
        z = random.random() * 3
        length = random.random() * 3
        if self.num_legs == 0:
            length = 0
        self.joints = []
        
        
        for i in range(0, self.num_links):
            if i == 0:
                self.Send_Cube(name="Body"+str(i), pos=[0,0,length+z/2] , size=[x,y,z], mass=1)  
            else:
                self.Send_Cube(name="Body"+str(i), pos=[0,y/2,0] , size=[x,y,z], mass=1)
            if i != self.num_links-1:
                if i == 0:
                    pyrosim.Send_Joint( name = "Body"+str(i)+"_Body"+str(i+1), parent= "Body"+str(i) , child = "Body"+str(i+1), type = "revolute", position = [0,y/2,length+z/2], jointAxis = "0 0 1")
                else:
                    pyrosim.Send_Joint( name = "Body"+str(i)+"_Body"+str(i+1), parent= "Body"+str(i) , child = "Body"+str(i+1), type = "revolute", position = [0,y,0], jointAxis = "0 0 1")
                self.joints.append("Body"+str(i)+"_Body"+str(i+1))
            if self.num_legs > 0:
                if i == 0:
                    pyrosim.Send_Joint( name = "Body"+str(i)+"_Leg"+str(i)+"right0", parent= "Body"+str(i) , child = "Leg"+str(i)+"right0", type = "revolute", position = [x/4,0,length], jointAxis = "1 0 0")
                    pyrosim.Send_Joint( name = "Body"+str(i)+"_Leg"+str(i)+"left0", parent= "Body"+str(i) , child = "Leg"+str(i)+"left0", type = "revolute", position = [-x/4,0,length], jointAxis = "1 0 0")
                else:
                    pyrosim.Send_Joint( name = "Body"+str(i)+"_Leg"+str(i)+"right0", parent= "Body"+str(i) , child = "Leg"+str(i)+"right0", type = "revolute", position = [x/4,y/2,-z/2], jointAxis = "1 0 0")
                    pyrosim.Send_Joint( name = "Body"+str(i)+"_Leg"+str(i)+"left0", parent= "Body"+str(i) , child = "Leg"+str(i)+"left0", type = "revolute", position = [-x/4,y/2,-z/2], jointAxis = "1 0 0")
                self.joints.append("Body"+str(i)+"_Leg"+str(i)+"right0")
                self.joints.append("Body"+str(i)+"_Leg"+str(i)+"left0")
            for j in range(0, self.num_legs):
                self.Send_Cube(name="Leg"+str(i)+"right"+str(j), pos=[0,0,-length/self.num_legs/2] , size=[0.2,0.2,length/self.num_legs], mass=1)
                self.Send_Cube(name="Leg"+str(i)+"left"+str(j), pos=[0,0,-length/self.num_legs/2] , size=[0.2,0.2,length/self.num_legs], mass=1)
                if j != self.num_legs-1:
                    pyrosim.Send_Joint( name = "Leg"+str(i)+"right"+str(j)+"_Leg"+str(i)+"right"+str(j+1), parent= "Leg"+str(i)+"right"+str(j) , child = "Leg"+str(i)+"right"+str(j+1), type = "revolute", position = [0,0,-length/self.num_legs], jointAxis = "1 0 0")
                    self.joints.append("Leg"+str(i)+"right"+str(j)+"_Leg"+str(i)+"right"+str(j+1))
                    pyrosim.Send_Joint( name = "Leg"+str(i)+"left"+str(j)+"_Leg"+str(i)+"left"+str(j+1), parent= "Leg"+str(i)+"left"+str(j) , child = "Leg"+str(i)+"left"+str(j+1), type = "revolute", position = [0,0,-length/self.num_legs], jointAxis = "1 0 0")
                    self.joints.append("Leg"+str(i)+"left"+str(j)+"_Leg"+str(i)+"left"+str(j+1))
            

        
        
        
        
        # # First body link
        # pyrosim.Send_Cube(name="Body0", pos=[0,0,length+z/2] , size=[x,y,z], mass=1)
        # # First body joint
        # pyrosim.Send_Joint( name = "Body0_Body1", parent= "Body0" , child = "Body1", type = "revolute", position = [0,y/2,length+z/2], jointAxis = "0 0 1")
        # self.joints.append("Body0_Body1")
        # # First body first leg joints
        # pyrosim.Send_Joint( name = "Body0_Leg0right0", parent= "Body0" , child = "Leg0right0", type = "revolute", position = [x/4,0,length], jointAxis = "0 1 0") 
        # self.joints.append("Body0_Leg0right0")
        # pyrosim.Send_Joint( name = "Body0_Leg0left0", parent= "Body0" , child = "Leg0left0", type = "revolute", position = [-x/4,0,length], jointAxis = "0 1 0")   
        # self.joints.append("Body0_Leg0left0")
        # # First body first leg links
        # pyrosim.Send_Cube(name="Leg0right0", pos=[0,0,-length/2], size=[0.2,0.2,length], mass=1)
        # pyrosim.Send_Cube(name="Leg0left0", pos=[0,0,-length/2], size=[0.2,0.2,length], mass=1)

        # for i in range(1, self.num_links):
        #     # Rest of body links
        #     pyrosim.Send_Cube(name="Body"+str(i), pos=[0,y/2,0], size=[x,y,z], mass=1)
        #     # Rest of body joints
        #     if i != self.num_links-1:
        #         pyrosim.Send_Joint( name = "Body"+str(i)+"_Body"+str(i+1), parent= "Body"+str(i) , child = "Body"+str(i+1), type = "revolute", position = [0,y,0], jointAxis = "0 0 1")
        #         self.joints.append("Body"+str(i-1)+"_Body"+str(i))
        #     # Rest of body first leg joints 
        #     pyrosim.Send_Joint( name = "Body"+str(i)+"_Leg"+str(i)+"right0", parent= "Body"+str(i) , child = "Leg"+str(i)+"0", type = "revolute", position = [x/4,y/2,-z/2], jointAxis = "0 1 0")
        #     self.joints.append("Body"+str(i)+"_Leg"+str(i)+"right0")
        #     pyrosim.Send_Joint( name = "Body"+str(i)+"_Leg"+str(i)+"left0", parent= "Body"+str(i) , child = "Leg"+str(i)+"1", type = "revolute", position = [-x/4,y/2,-z/2], jointAxis = "0 1 0")
        #     self.joints.append("Body"+str(i)+"_Leg"+str(i)+"left0")
        #     # Rest of body first leg links
        #     # Rest of body rest of leg joints
            
        #     for j in range(0, self.num_legs):
        #         pyrosim.Send_Cube(name="Leg"+str(i)+"right"+str(j), pos=[0,0,-length/2], size=[.2,.2,length], mass=1)
        #         pyrosim.Send_Cube(name="Leg"+str(i)+"left"+str(j), pos=[0,0,-length/2], size=[.2,.2,length], mass=1)
        #         if j != self.num_legs-1:
        #             pyrosim.Send_Joint( name = "Leg"+str(i)+"right"+str(j)+"_Leg"+str(i)+"right"+str(j+1), parent= "Leg"+str(i)+"right"+str(j) , child = "Leg"+str(i)+"right"+str(j+1), type = "revolute", position = [0,0,-length/2], jointAxis = "0 1 0")
        #             self.joints.append("Leg"+str(i)+"right"+str(j)+"_Leg"+str(i)+"right"+str(j+1))
        #             pyrosim.Send_Joint( name = "Leg"+str(i)+"left"+str(j)+"_Leg"+str(i)+"left"+str(j+1), parent= "Leg"+str(i)+"left"+str(j) , child = "Leg"+str(i)+"left"+str(j+1), type = "revolute", position = [0,0,-length/2], jointAxis = "0 1 0")
        #             self.joints.append("Leg"+str(i)+"left"+str(j)+"_Leg"+str(i)+"left"+str(j+1))
            
            

        #     pyrosim.Send_Cube(name="Leg"+str(i)+"right0", pos=[0,0,-length/2], size=[.2,.2,length], mass=1)
        #     pyrosim.Send_Cube(name="Leg"+str(i)+"left0", pos=[0,0,-length/2], size=[.2,.2,length], mass=1)        

        #     pyrosim.Send_Joint( name = "Leg"+str(i)+"right0_Leg"+str(i)+"right1", parent= "Leg"+str(i)+"right0" , child = "Leg"+str(i)+"right1", type = "revolute", position = [0,0,-length/2], jointAxis = "0 1 0")
        #     self.joints.append("Leg"+str(i)+"right0_Leg"+str(i)+"right1")
        #     pyrosim.Send_Joint( name = "Leg"+str(i)+"left0_Leg"+str(i)+"left1", parent= "Leg"+str(i)+"left0" , child = "Leg"+str(i)+"left1", type = "revolute", position = [0,0,-length/2], jointAxis = "0 1 0")
        #     self.joints.append("Leg"+str(i)+"left0_Leg"+str(i)+"left1")



        # if (0,0) in self.rand_links:
        #     pyrosim.Send_Cube(name="Link(0,0)", pos=[0,0,1+max(self.Legs)] , size=[self.Xs[(0,0)],self.Ys[(0,0)],1], color = "green")
        # else:
        #     pyrosim.Send_Cube(name="Link(0,0)", pos=[0,0,1+max(self.Legs)] , size=[self.Xs[(0,0)],self.Ys[(0,0)],1])
        # pyrosim.Send_Joint( name = "Link(0,0)_Link(0,1)", parent= "Link(0,0)" , child = "Link(0,1)", type = "revolute", position = [0,self.Ys[(0,0)]/2,1+max(self.Legs)], jointAxis = "0 0 1")
        # self.joints.append("Link(0,0)_Link(0,1)")
        # pyrosim.Send_Joint( name = "Link(0,0)_Link(1,0)", parent= "Link(0,0)" , child = "Link(1,0)", type = "revolute", position = [self.Xs[(0,0)]/2,0,1+max(self.Legs)], jointAxis = "0 0 1")
        # self.joints.append("Link(0,0)_Link(1,0)")
        # pyrosim.Send_Joint( name = "Link(0,0)_Link(1,1)", parent= "Link(0,0)" , child = "Link(1,1)", type = "revolute", position = [self.Xs[(0,0)]/2,self.Ys[(0,0)]/2,1+max(self.Legs)], jointAxis = "0 0 1")
        # self.joints.append("Link(0,0)_Link(1,1)")
        # if (1,1) in self.rand_links:
        #     pyrosim.Send_Cube(name = "Link(1,1)", pos = [self.Xs[(1,1)]/2,self.Ys[(1,1)]/2,0], size = [self.Xs[(1,1)],self.Ys[(1,1)],1], color = "green")
        # else:
        #     pyrosim.Send_Cube(name = "Link(1,1)", pos = [self.Xs[(1,1)]/2,self.Ys[(1,1)]/2,0], size = [self.Xs[(1,1)],self.Ys[(1,1)],1])                  
        
        # pyrosim.Send_Joint( name = "Link(0,0)_LinkUnder0", parent= "Link(0,0)" , child = "LinkUnder0", type = "revolute", position = [0,0,0.5+max(self.Legs)], jointAxis = "0 0 1")
        # self.joints.append("Link(0,0)_LinkUnder0")
        # if "Under0" in self.rand_links:
        #     pyrosim.Send_Cube(name="LinkUnder0", pos=[0,0,-1/2] , size=[1,1,1], color = "green")
        # else:
        #     pyrosim.Send_Cube(name="LinkUnder0", pos=[0,0,-1/2] , size=[1,1,1])

        # pyrosim.Send_Joint( name = "Link(1,1)_LinkUnder1", parent= "Link(1,1)" , child = "LinkUnder1", type = "revolute", position = [1/2,1/2,-1/2], jointAxis = "0 0 1")
        # self.joints.append("Link(1,1)_LinkUnder1")
        # if "Under1" in self.rand_links:
        #     pyrosim.Send_Cube(name="LinkUnder1", pos=[0,0,-1/2] , size=[1,1,1], color = "green")
        # else:
        #     pyrosim.Send_Cube(name="LinkUnder1", pos=[0,0,-1/2] , size=[1,1,1])
    
        # for i in range(1, self.num_links-1):
        #     pyrosim.Send_Joint( name = "Link(" + str(i) + ",0)_Link(" + str(i+1) + ",0)", parent= "Link(" + str(i) + ",0)" , child = "Link(" + str(i+1) + ",0)", type = "revolute", position = [self.Xs[(i,0)],0,0], jointAxis = "0 0 1")
        #     self.joints.append("Link(" + str(i) + ",0)_Link(" + str(i+1) + ",0)")

        # for j in range(1, self.num_links-1):
        #     pyrosim.Send_Joint( name = "Link(0," + str(j) + ")_Link(0," + str(j+1) + ")", parent= "Link(0," + str(j) + ")" , child = "Link(0," + str(j+1) + ")", type = "revolute", position = [0,self.Ys[(0,j)],0], jointAxis = "0 0 1")
        #     self.joints.append("Link(0," + str(j) + ")_Link(0," + str(j+1) + ")")

        # for i in range(1, self.num_links):
        #     if (i,0) in self.rand_links:
        #         pyrosim.Send_Cube(name="Link(" + str(i) + ",0)", pos=[self.Xs[(i,0)]/2,0,0] , size=[self.Xs[(i,0)],self.Ys[(i,0)],1], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="Link(" + str(i) + ",0)", pos=[self.Xs[(i,0)]/2,0,0] , size=[self.Xs[(i,0)],self.Ys[(i,0)],1])

        # for j in range(1, self.num_links):
        #     if (0,j) in self.rand_links:
        #         pyrosim.Send_Cube(name="Link(0," + str(j) + ")", pos=[0,self.Ys[(0,j)]/2,0] , size=[self.Xs[(0,j)],self.Ys[(0,j)],1], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="Link(0," + str(j) + ")", pos=[0,self.Ys[(0,j)]/2,0] , size=[self.Xs[(0,j)],self.Ys[(0,j)],1])

        # for i in range(1, self.num_links - 1):
        #     pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(i) + ")_Link(" + str(i+1) + "," + str(i+1) + ")", parent= "Link(" + str(i) + "," + str(i) + ")" , child = "Link(" + str(i+1) + "," + str(i+1) + ")", type = "revolute", position = [self.Xs[(i,i)],self.Ys[(i,i)],0], jointAxis = "0 0 1")
        #     self.joints.append("Link(" + str(i) + "," + str(i) + ")_Link(" + str(i+1) + "," + str(i+1) + ")")
        #     if (i+1,i+1) in self.rand_links:
        #         pyrosim.Send_Cube(name="Link(" + str(i+1) + "," + str(i+1) + ")", pos=[self.Xs[(i+1,i+1)]/2,self.Ys[(i+1,i+1)]/2,0] , size=[self.Xs[(i+1,i+1)],self.Ys[(i+1,i+1)],1], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="Link(" + str(i+1) + "," + str(i+1) + ")", pos=[self.Xs[(i+1,i+1)]/2,self.Ys[(i+1,i+1)]/2,0] , size=[self.Xs[(i+1,i+1)],self.Ys[(i+1,i+1)],1])
            
        #     pyrosim.Send_Joint( name = "Link(" + str(i+1) + "," + str(i+1) + ")_LinkUnder" + str(i+1), parent= "Link(" + str(i+1) + "," + str(i+1) + ")" , child = "LinkUnder" + str(i+1), type = "revolute", position = [1/2,1/2,-1/2], jointAxis = "0 0 1")
        #     self.joints.append("Link(" + str(i+1) + "," + str(i+1) + ")_LinkUnder" + str(i+1))
        #     pyrosim.Send_Cube(name="LinkUnder" + str(i+1), pos=[0,0,-1/2] , size=[1,1,1])

        #     pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(i) + ")_Link(" + str(i+1) + "," + str(i) + ")", parent= "Link(" + str(i) + "," + str(i) + ")" , child = "Link(" + str(i+1) + "," + str(i) + ")", type = "revolute", position = [self.Xs[(i,i)],self.Ys[(i,i)]/2,0], jointAxis = "0 0 1")
        #     self.joints.append("Link(" + str(i) + "," + str(i) + ")_Link(" + str(i+1) + "," + str(i) + ")")
        #     pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(i) + ")_Link(" + str(i) + "," + str(i+1) + ")", parent= "Link(" + str(i) + "," + str(i) + ")" , child = "Link(" + str(i) + "," + str(i+1) + ")", type = "revolute", position = [self.Xs[(i,i)]/2,self.Ys[(i,i)],0], jointAxis = "0 0 1")
        #     self.joints.append("Link(" + str(i) + "," + str(i) + ")_Link(" + str(i) + "," + str(i+1) + ")")
        #     if (i+1,i) in self.rand_links:
        #         pyrosim.Send_Cube(name="Link(" + str(i+1) + "," + str(i) + ")", pos=[self.Xs[(i+1,i)]/2,0,0] , size=[self.Xs[(i+1,i)],self.Ys[(i+1,i)],1], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="Link(" + str(i+1) + "," + str(i) + ")", pos=[self.Xs[(i+1,i)]/2,0,0] , size=[self.Xs[(i+1,i)],self.Ys[(i+1,i)],1])
        #     if (i,i+1) in self.rand_links:
        #         pyrosim.Send_Cube(name="Link(" + str(i) + "," + str(i+1) + ")", pos=[0,self.Ys[(i,i+1)]/2,0] , size=[self.Xs[(i,i+1)],self.Ys[(i,i+1)],1], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="Link(" + str(i) + "," + str(i+1) + ")", pos=[0,self.Ys[(i,i+1)]/2,0] , size=[self.Xs[(i,i+1)],self.Ys[(i,i+1)],1])

        #     for x in range(i+1, self.num_links-1):
        #         pyrosim.Send_Joint( name = "Link(" + str(x) + "," + str(i) + ")_Link(" + str(x+1) + "," + str(i) + ")", parent= "Link(" + str(x) + "," + str(i) + ")" , child = "Link(" + str(x+1) + "," + str(i) + ")", type = "revolute", position = [self.Xs[(x,i)],0,0], jointAxis = "0 0 1")
        #         self.joints.append("Link(" + str(x) + "," + str(i) + ")_Link(" + str(x+1) + "," + str(i) + ")")
        #         if (x+1,i) in self.rand_links:
        #             pyrosim.Send_Cube(name="Link(" + str(x+1) + "," + str(i) + ")", pos=[self.Xs[(x+1,i)]/2,0,0] , size=[self.Xs[(x+1,i)],self.Ys[(x+1,i)],1], color = "green")
        #         else:
        #             pyrosim.Send_Cube(name="Link(" + str(x+1) + "," + str(i) + ")", pos=[self.Xs[(x+1,i)]/2,0,0] , size=[self.Xs[(x+1,i)],self.Ys[(x+1,i)],1])

        #     for y in range(i+1, self.num_links-1):
        #         pyrosim.Send_Joint( name = "Link(" + str(i) + "," + str(y) + ")_Link(" + str(i) + "," + str(y+1) + ")", parent= "Link(" + str(i) + "," + str(y) + ")" , child = "Link(" + str(i) + "," + str(y+1) + ")", type = "revolute", position = [0,self.Ys[(i,y)],0], jointAxis = "0 0 1")
        #         self.joints.append("Link(" + str(i) + "," + str(y) + ")_Link(" + str(i) + "," + str(y+1) + ")")
        #         if (i,y+1) in self.rand_links:
        #             pyrosim.Send_Cube(name="Link(" + str(i) + "," + str(y+1) + ")", pos=[0,self.Ys[(i,y+1)]/2,0] , size=[self.Xs[(i,y+1)],self.Ys[(i,y+1)],1], color = "green")
        #         else:
        #             pyrosim.Send_Cube(name="Link(" + str(i) + "," + str(y+1) + ")", pos=[0,self.Ys[(i,y+1)]/2,0] , size=[self.Xs[(i,y+1)],self.Ys[(i,y+1)],1])
        
        # for i in range(self.num_links):
        #     pyrosim.Send_Joint( name = "LinkUnder" + str(i) + "_LinkArm" + str(i) + str(0) , parent= "LinkUnder" + str(i) , child = "LinkArm" + str(i) + str(0) , type = "revolute", position = [1/2,0,-1/2], jointAxis = "0 1 0")
        #     self.joints.append("LinkUnder" + str(i) + "_LinkArm" + str(i) + str(0))
        #     pyrosim.Send_Joint( name = "LinkUnder" + str(i) + "_LinkArm" + str(i) + str(1) , parent= "LinkUnder" + str(i) , child = "LinkArm" + str(i) + str(1) , type = "revolute", position = [-1/2,0,-1/2], jointAxis = "0 1 0")
        #     self.joints.append("LinkUnder" + str(i) + "_LinkArm" + str(i) + str(1))
        #     pyrosim.Send_Joint( name = "LinkUnder" + str(i) + "_LinkArm" + str(i) + str(2) , parent= "LinkUnder" + str(i) , child = "LinkArm" + str(i) + str(2) , type = "revolute", position = [0,1/2,-1/2], jointAxis = "1 0 0")
        #     self.joints.append("LinkUnder" + str(i) + "_LinkArm" + str(i) + str(2))
        #     pyrosim.Send_Joint( name = "LinkUnder" + str(i) + "_LinkArm" + str(i) + str(3) , parent= "LinkUnder" + str(i) , child = "LinkArm" + str(i) + str(3) , type = "revolute", position = [0,-1/2,-1/2], jointAxis = "1 0 0")
        #     self.joints.append("LinkUnder" + str(i) + "_LinkArm" + str(i) + str(3))

        #     if 'Arm'+str(i)+'0' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(0), pos=[self.Arms[i*4]/2,0,0] , size=[self.Arms[i*4],0.2,0.2], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(0), pos=[self.Arms[i*4]/2,0,0] , size=[self.Arms[i*4],0.2,0.2])
        #     if 'Arm'+str(i)+'1' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(1), pos=[-self.Arms[i*4+1]/2,0,0] , size=[self.Arms[i*4+1],0.2,0.2], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(1), pos=[-self.Arms[i*4+1]/2,0,0] , size=[self.Arms[i*4+1],0.2,0.2])
        #     if 'Arm'+str(i)+'2' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(2), pos=[0,self.Arms[i*4+2]/2,0] , size=[0.2,self.Arms[i*4+2],0.2], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(2), pos=[0,self.Arms[i*4+2]/2,0] , size=[0.2,self.Arms[i*4+2],0.2])
        #     if 'Arm'+str(i)+'3' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(3), pos=[0,-self.Arms[i*4+3]/2,0] , size=[0.2,self.Arms[i*4+3],0.2], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkArm" + str(i) + str(3), pos=[0,-self.Arms[i*4+3]/2,0] , size=[0.2,self.Arms[i*4+3],0.2])

        #     pyrosim.Send_Joint(name= "LinkArm" + str(i) + str(0) + "_LinkLeg" + str(i) + str(0), parent= "LinkArm" + str(i) + str(0) , child = "LinkLeg" + str(i) + str(0) , type = "revolute", position = [self.Arms[i*4],0,0], jointAxis = "0 1 0")
        #     self.joints.append("LinkArm" + str(i) + str(0) + "_LinkLeg" + str(i) + str(0))
        #     pyrosim.Send_Joint(name= "LinkArm" + str(i) + str(1) + "_LinkLeg" + str(i) + str(1), parent= "LinkArm" + str(i) + str(1) , child = "LinkLeg" + str(i) + str(1) , type = "revolute", position = [-self.Arms[i*4+1],0,0], jointAxis = "0 1 0")
        #     self.joints.append("LinkArm" + str(i) + str(1) + "_LinkLeg" + str(i) + str(1))
        #     pyrosim.Send_Joint(name= "LinkArm" + str(i) + str(2) + "_LinkLeg" + str(i) + str(2), parent= "LinkArm" + str(i) + str(2) , child = "LinkLeg" + str(i) + str(2) , type = "revolute", position = [0,-self.Arms[i*4+2],0], jointAxis = "1 0 0")
        #     self.joints.append("LinkArm" + str(i) + str(2) + "_LinkLeg" + str(i) + str(2))
        #     pyrosim.Send_Joint(name= "LinkArm" + str(i) + str(3) + "_LinkLeg" + str(i) + str(3), parent= "LinkArm" + str(i) + str(3) , child = "LinkLeg" + str(i) + str(3) , type = "revolute", position = [0,-self.Arms[i*4+3],0], jointAxis = "1 0 0")
        #     self.joints.append("LinkArm" + str(i) + str(3) + "_LinkLeg" + str(i) + str(3))

        #     if 'Leg'+str(i)+'0' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(0), pos=[0,0,-self.Legs[i*4]/2] , size=[0.2,0.2,self.Legs[i*4]], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(0), pos=[0,0,-self.Legs[i*4]/2] , size=[0.2,0.2,self.Legs[i*4]])
        #     if 'Leg'+str(i)+'1' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(1), pos=[0,0,-self.Legs[i*4+1]/2] , size=[0.2,0.2,self.Legs[i*4+1]], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(1), pos=[0,0,-self.Legs[i*4+1]/2] , size=[0.2,0.2,self.Legs[i*4+1]])
        #     if 'Leg'+str(i)+'2' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(2), pos=[0,0,-self.Legs[i*4+2]/2] , size=[0.2,0.2,self.Legs[i*4+2]], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(2), pos=[0,0,-self.Legs[i*4+2]/2] , size=[0.2,0.2,self.Legs[i*4+2]])
        #     if 'Leg'+str(i)+'3' in self.rand_links:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(3), pos=[0,0,-self.Legs[i*4+3]/2] , size=[0.2,0.2,self.Legs[i*4+3]], color = "green")
        #     else:
        #         pyrosim.Send_Cube(name="LinkLeg" + str(i) + str(3), pos=[0,0,-self.Legs[i*4+3]/2] , size=[0.2,0.2,self.Legs[i*4+3]])


        pyrosim.End()

    def Create_Brain(self):
        s = str(self.myID)
        f = open("brain" + s + ".nndf", "w")
        f.close()
        pyrosim.Start_NeuralNetwork("brain" + s + ".nndf")
        
        
        for ind, rand in enumerate(self.rand_links):
            pyrosim.Send_Sensor_Neuron(name =  self.numJoints + ind, linkName = rand)
        for i, Jname in enumerate(self.joints):
            pyrosim.Send_Motor_Neuron(name = i, jointName = Jname)
        # print(self.weights.shape, "weight SHAPE")
        # print((len(self.rand_links), self.numJoints), "shape")
        for currentRow in range(len(self.rand_links)):
            for currentCol in range(self.numJoints):
                pyrosim.Send_Synapse(sourceNeuronName = self.numJoints + currentRow, targetNeuronName = currentCol, weight = self.weights[currentRow][currentCol] )
        

        pyrosim.End()

    def Mutate(self):
        if len(self.rand_links) > 1:
            randRow = random.randint(0,len(self.rand_links) - 1)
            randColumn = random.randint(0,self.numJoints- 1)
            number = random.randint(0, 6)
        #number = 13
        else:
            number = random.randint(1,6)
        print(number, "number!")

        if number == 0:
            self.weights[randRow][randColumn] = random.random() * 2 - 1
            print("mutated weight")
        elif number == 1:
            self.links.append("Body" + str(self.num_links))
            for i in range(self.num_legs):
                self.links.append("Leg"+str(self.num_links)+"right"+str(i))
                self.links.append("Leg"+str(self.num_links)+"left"+str(i))
            self.num_links += 1
            print("added body")
        elif number == 2:
            if self.num_links == 1:
                self.Mutate()
                return
            if self.num_links == 2 and self.num_legs == 0:
                self.Mutate()
                return
            self.num_links -= 1
            self.links.remove("Body" + str(self.num_links))
            for i in range(self.num_legs):
                self.links.remove("Leg"+str(self.num_links)+"right"+str(i))
                self.links.remove("Leg"+str(self.num_links)+"left"+str(i))
            if "Body" + str(self.num_links) in self.rand_links:
                indx = self.rand_links.index("Body" + str(self.num_links))
                self.rand_links.remove("Body" + str(self.num_links))
                self.weights = numpy.delete(self.weights, indx, 0)
            
            for i in range(self.num_legs):
                if "Leg"+str(self.num_links)+"right"+str(i) in self.rand_links:
                    indx = self.rand_links.index("Leg"+str(self.num_links)+"right"+str(i))
                    self.rand_links.remove("Leg"+str(self.num_links)+"right"+str(i))
                    self.weights = numpy.delete(self.weights, indx, 0)
                if "Leg"+str(self.num_links)+"left"+str(i) in self.rand_links:
                    indx = self.rand_links.index("Leg"+str(self.num_links)+"left"+str(i))
                    self.rand_links.remove("Leg"+str(self.num_links)+"left"+str(i))
                    self.weights = numpy.delete(self.weights, indx, 0)
            print("removed body", self.num_links, "left")
        elif number == 3:
            self.num_legs += 1
            for i in range(self.num_links):
                self.links.append("Leg"+str(i)+"right"+str(self.num_legs-1))
                self.links.append("Leg"+str(i)+"left"+str(self.num_legs-1))
            print("added leg", self.num_legs, "legs")
        elif number == 4:
            if self.num_legs == 0:
                self.Mutate()
                return
            if self.num_legs == 1 and self.num_links == 1:
                self.Mutate()
                return
            self.num_legs -= 1
            for i in range(self.num_links):
                self.links.remove("Leg"+str(i)+"right"+str(self.num_legs))
                self.links.remove("Leg"+str(i)+"left"+str(self.num_legs))
                if "Leg"+str(i)+"right"+str(self.num_legs) in self.rand_links:
                    indx = self.rand_links.index("Leg"+str(i)+"right"+str(self.num_legs))
                    self.rand_links.remove("Leg"+str(i)+"right"+str(self.num_legs))
                    self.weights = numpy.delete(self.weights, indx, 0)
                if "Leg"+str(i)+"left"+str(self.num_legs) in self.rand_links:
                    indx = self.rand_links.index("Leg"+str(i)+"left"+str(self.num_legs))
                    self.rand_links.remove("Leg"+str(i)+"left"+str(self.num_legs))
                    self.weights = numpy.delete(self.weights, indx, 0)
            print("removed leg", self.num_legs, "legs left")
        elif number == 5:
            if len(self.links) == len(self.rand_links):
                self.Mutate()
                return
            ind = random.randint(0,len(self.links)-1)
            while self.links[ind] in self.rand_links:
                ind = random.randint(0,len(self.links)-1)
            self.rand_links.append(self.links[ind])
            new_arr = [numpy.random.random(self.numJoints)]
            self.weights = numpy.concatenate((self.weights, new_arr))
            print("added sensor")
        elif number == 6:
            if len(self.rand_links) == 0:
                self.Mutate()   
                return         
            ind = random.randint(0,len(self.rand_links)-1)
            self.rand_links.remove(self.rand_links[ind])
            self.weights = numpy.delete(self.weights, ind, 0)
            print("removed sensor")
        # elif number == 1:
        #     self.Xs[(random.randint(0,self.num_links-1), random.randint(0,self.num_links-1))] = random.random()
        # elif number == 2:
        #     self.Ys[(random.randint(0,self.num_links-1), random.randint(0,self.num_links-1))] = random.random()
        # elif number == 3:
        #     self.Arms[random.randint(0,self.num_links*4-1)] = random.random() * 0.5
        # elif number == 4:
        #     self.Legs[random.randint(0,self.num_links*4-1)] = random.random() * 2
        # elif number == 5:
        #     del self.rand_links[random.randint(0,len(self.rand_links)-1)]
        # # elif number == 5:
        # #     self.rand_links[random.randint(0,len(self.rand_links)-1)] = (random.randint(0,self.num_links-1), random.randint(0,self.num_links-1))
        # # elif number == 6:
        # #     self.rand_links[random.randint(0,len(self.rand_links)-1)] = 'Arm'+str(random.randint(0,self.num_links-1))+str(random.randint(0,3))
        # # elif number == 7:
        # #     self.rand_links[random.randint(0,len(self.rand_links)-1)] = 'Leg'+str(random.randint(0,self.num_links-1))+str(random.randint(0,3))
        # elif number == 8:
        #     self.rand_links.append((random.randint(0,self.num_links-1), random.randint(0,self.num_links-1)))
        #     while list(set(self.rand_links)) != self.rand_links:
        #         self.rand_links.append((random.randint(0,self.num_links-1), random.randint(0,self.num_links-1)))
        #     self.rand_links = list(set(self.rand_links))
        # elif number == 9:
        #     self.rand_links.append('Arm'+str(random.randint(0,self.num_links-1))+str(random.randint(0,3)))
        #     while list(set(self.rand_links)) != self.rand_links:
        #         self.rand_links.append('Arm'+str(random.randint(0,self.num_links-1))+str(random.randint(0,3)))
        #     self.rand_links = list(set(self.rand_links))
        # elif number == 10:
        #     self.rand_links.append('Leg'+str(random.randint(0,self.num_links-1))+str(random.randint(0,3)))
        #     while list(set(self.rand_links)) != self.rand_links:
        #         self.rand_links.append('Leg'+str(random.randint(0,self.num_links-1))+str(random.randint(0,3)))
        #     self.rand_links = list(set(self.rand_links))
        # elif number == 11:
        #     self.rand_links.pop(random.randint(0,len(self.rand_links)-1))
        # elif number == 12:
        #     self.num_links += 1
        # elif number == 13:
        #     self.num_links -= 1

    def Set_ID(self, id):
        
        self.myID = id
    
    def Start_Simulation(self, directOrGUI):
        # while not os.path.exists("world" + str(self.myID) + ".sdf"):
        #     time.sleep(0.01)
        # while not os.path.exists("body.urdf"):
        #     time.sleep(0.01)
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGUI +" " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        filename = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(filename):
            time.sleep(0.01)
        assert os.path.isfile(filename)
        f = open(filename, "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()
        os.system("del fitness"+str(self.myID)+".txt")

    def Compute_Fitness(self):
        return self.fitness