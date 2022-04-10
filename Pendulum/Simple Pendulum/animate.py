import numpy as np
from vpython import *

array=np.genfromtxt('data.csv',delimiter=',')
ball= sphere(pos=vector(array[1][0],-array[2][0],0),radius=0.2,color=color.green,make_trail=True,retain=20)
roof=sphere(pos=vector(0,1,0),radius=0.09,color=color.red)
pos1=vector(0,1,0)
rod=cylinder(pos=vector(0,1,0),axis=ball.pos-pos1,radius=0.025)
        
i=0
a=input("Press enter to start: ")

while (i<=len(array[0])):
    rate(60)
    ball.pos=vector(array[1][i],-array[2][i],0)
    rod.axis=ball.pos-rod.pos
    i+=1
        
