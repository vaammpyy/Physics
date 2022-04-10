import numpy as np
from vpython import *

array=np.genfromtxt('data.csv',delimiter=',')
ball1= sphere(pos=vector(array[0][0],array[1][0],array[2][0]),radius=0.1,color=color.green,make_trail=True,retain=20)
ball2= sphere(pos=vector(array[6][0],array[7][0],array[8][0]),radius=0.2,color=color.yellow,make_trail=True,retain=20)

i=0
a=input("Press enter to start: ")

while (i<=len(array[0])):
    rate(500)
    ball1.pos=vector(array[0][i],array[1][i],array[2][i])
    ball2.pos=vector(array[6][i],array[7][i],array[8][i])
    i+=1
