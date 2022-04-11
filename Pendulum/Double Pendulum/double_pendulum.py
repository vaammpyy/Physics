import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from vpython import *

print("Solving the Lagrangian")

t, m1,l1,m2,l2,g=smp.symbols("t, m_1 l_1 m_2 l_2 g")
theta1,theta2=smp.symbols(r" \theta_1 \theta_2",cls=smp.Function)
theta1=theta1(t)
theta2=theta2(t)
d_theta1=smp.diff(theta1,t)
d_theta2=smp.diff(theta2,t)
dd_theta1=smp.diff(d_theta1,t)
dd_theta2=smp.diff(d_theta2,t)

x1=l1*smp.sin(theta1)
y1=-l1*smp.cos(theta1)
x2=l1*smp.sin(theta1)+l2*smp.sin(theta2)
y2=-l1*smp.cos(theta1)-l2*smp.cos(theta2)

T_1=smp.Rational(1,2)*m1*(smp.diff(x1,t)**2+smp.diff(y1,t)**2)
V_1=m1*g*y1
T_2=m2*smp.Rational(1,2)*(smp.diff(x2,t)**2+smp.diff(y2,t)**2)
V_2=m2*g*y2

L=T_1+T_2-V_1-V_2

LE1= smp.diff(L,theta1)-smp.diff(smp.diff(L,d_theta1),t)
LE2= smp.diff(L,theta2)-smp.diff(smp.diff(L,d_theta2),t)

solutions=smp.solve([LE1,LE2],(dd_theta1,dd_theta2),rational=False,simplify=False)
print("Completed!!")

domega1_dt_f=smp.lambdify([t,g,m1,l1,m2,l2,theta1,theta2,d_theta1,d_theta2],solutions[dd_theta1])
domega2_dt_f=smp.lambdify([t,g,m1,l1,m2,l2,theta1,theta2,d_theta1,d_theta2],solutions[dd_theta2])
dtheta1_dt_f=smp.lambdify(d_theta1,d_theta1)
dtheta2_dt_f=smp.lambdify(d_theta2,d_theta2)

def dSdt(S,t,g,m1,l1,m2,l2):
    return(dtheta1_dt_f(S[2]),dtheta2_dt_f(S[3]),domega1_dt_f(t,g,m1,l1,m2,l2,S[0],S[1],S[2],S[3]),domega2_dt_f(t,g,m1,l1,m2,l2,S[0],S[1],S[2],S[3]))

m1=float(input("Enter the mass of Particle 1: "))
l1=float(input("Enter the length of Particle 1: "))
t_1=float(input("Enter the intial angle of Particle 1: "))
dt_1=float(input("Enter the intial angular velocity of Particle 1: "))
m2=float(input("Enter the mass of Particle 2: "))
l2=float(input("Enter the length of Particle 2: "))
t_2=float(input("Enter the intial angle of Particle 2: "))
dt_2=float(input("Enter the intial angular velocity of Particle 2: "))

t_1=np.pi/180*t_1
dt_1=np.pi/180*dt_1
t_2=np.pi/180*t_2
dt_2=np.pi/180*dt_2

t_end=float(input("Enter the end time: "))
dt=float(input("Enter time step: "))

t=np.linspace(0,t_end,int(t_end/dt))

g=9.8


print("Numerically integrating")

sols=odeint(dSdt,y0=[t_1,t_2,dt_1,dt_2],t=t,args=(g,m1,l1,m2,l2))

ans=sols.T

def get_cart(theta1,theta2):
    return(l1*np.sin(theta1),-l1*np.cos(theta1),l1*np.sin(theta1)+l2*np.sin(theta2),-l1*np.cos(theta1)-l2*np.cos(theta2))

cart=get_cart(ans[0],ans[1])

print("Completed!!")

canvas(width=1000,height=600)

array=cart
ball1= sphere(pos=vector(array[0][0],array[1][0],0),radius=m1/10,color=color.green,make_trail=False,retain=20)
ball2= sphere(pos=vector(array[2][0],array[3][0],0),radius=m2/10,color=color.cyan,make_trail=True,trail_color=color.orange)
roof=sphere(pos=vector(0,0,0),radius=0.09,color=color.red)
pos1=vector(0,0,0)
rod1=cylinder(pos=vector(0,0,0),axis=ball1.pos-pos1,radius=0.025)
rod2=cylinder(pos=ball1.pos,axis=ball2.pos-ball1.pos,radius=0.025)
        
i=0

a=input("Press enter to start: ")

while (i<=len(array[0])):
    rate(int(1/dt))
    ball1.pos=vector(array[0][i],array[1][i],0)
    ball2.pos=vector(array[2][i],array[3][i],0)
    rod1.axis=ball1.pos-rod1.pos
    rod2.pos=ball1.pos
    rod2.axis=ball2.pos-rod2.pos
    i+=1
