#coding=utf-8
import math;

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

v0=float(input('v_0>'));
theta=float(input('θ>'));
g=float(input('g>'));
m=float(input('m>'));
k=float(input('k>'));
rate=float(input('rate(/s)>'));

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
    
    print(t,x,y,vx,vy,ax,ay);
    
print('t:',t);

df.to_csv('result.csv',index=False);

df.plot.scatter(x='x',y='y');
plt.show();
