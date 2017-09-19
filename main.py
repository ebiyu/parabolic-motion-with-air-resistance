#coding=utf-8
import math;

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

print('t x y vx vy ax ay');

f=open('result.csv','w');

while(y>=0):
    ax=(-k*vx)/m;
    ay=(-m*g-k*vy)/m;
    
    t+=1/rate;
    
    vx+=ax/rate;
    vy+=ay/rate;
    x+=vx/rate;
    y+=vy/rate;
    
    print(t,x,y,vx,vy,ax,ay);
    f.write(str(t));
    f.write(str(','));
    f.write(str(x));
    f.write(str(','));
    f.write(str(y));
    f.write(str(','));
    f.write(str(vx));
    f.write(str(','));
    f.write(str(vy));
    f.write(str(','));
    f.write(str(ax));
    f.write(str(','));
    f.write(str(ay));
    f.write(str('\n'));
    
print('t:',t);
f.close();
