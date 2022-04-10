import numpy as np
from vpython import *
import random


ball=sphere(pos=vector(0,0,0),color=color.red,radius=1,make_trail=True,trail_color=color.green,retain=20)

ch=np.linspace(-1,1,2000)

i=0

a=input("Press enter to start: ")

while(i<1000):
    rate(30)
    ball.pos=ball.pos+vector(random.choice(ch),random.choice(ch),random.choice(ch))
    i+=1
