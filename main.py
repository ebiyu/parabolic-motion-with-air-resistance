#coding=utf-8
import math;

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import sys
args=sys.argv
if(len(args)!=7):
    print('Error!');
    exit()

v0=float(args[1])
thetadeg=float(args[2])
theta=thetadeg/360*2*3.14;
g=float(args[3])
m=float(args[4])
k=float(args[5])
rate=float(args[6])

t=0;
x=0;
y=0;

vx=v0*math.cos(theta);
vy=v0*math.sin(theta);
ax=0;
ay=0;

df=pd.DataFrame(columns=['t','x','y','vx','vy','ax','ay']);

while(y>=0):
    ax=(-k*vx)/m;
    ay=(-m*g-k*vy)/m;
    
    t+=1/rate;
    
    vx+=ax/rate;
    vy+=ay/rate;
    x+=vx/rate;
    y+=vy/rate;
    
    df2=pd.DataFrame([[t,x,y,vx,vy,ax,ay]],columns=['t','x','y','vx','vy','ax','ay']);
    df=df.append(df2);
    
print('t:',t);
print('x:',x);

df.to_csv('result/'+str(v0)+'-'+str(thetadeg)+'-'+str(g)+'-'+str(m)+'-'+str(k)+'-'+str(rate)+'.csv',index=False);

df.plot.scatter(x='x',y='y');
plt.axes().set_aspect('equal',adjustable='box');
plt.xlim(xmin=0);
plt.ylim(ymin=0);
plt.show();
