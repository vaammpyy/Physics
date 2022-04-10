import numpy as np
from vpython import *

array=np.genfromtxt('data.csv',delimiter=',')
ball1= sphere(pos=vector(array[0][0],array[1][0],0),radius=0.2,color=color.green,make_trail=True,retain=20)
ball2= sphere(pos=vector(array[2][0],array[3][0],0),radius=0.4,color=color.blue,make_trail=True,retain=20)
roof=sphere(pos=vector(0,0,0),radius=0.09,color=color.red)
pos1=vector(0,0,0)
rod1=cylinder(pos=vector(0,0,0),axis=ball1.pos-pos1,radius=0.025)
rod2=cylinder(pos=ball1.pos,axis=ball2.pos-ball1.pos,radius=0.025)
        
i=0
a=input("Press enter to start: ")

while (i<=len(array[0])):
    rate(120)
    ball1.pos=vector(array[0][i],array[1][i],0)
    ball2.pos=vector(array[2][i],array[3][i],0)
    rod1.axis=ball1.pos-rod1.pos
    rod2.pos=ball1.pos
    rod2.axis=ball2.pos-rod2.pos
    i+=1
