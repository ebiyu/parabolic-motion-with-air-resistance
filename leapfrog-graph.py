#coding=utf-8
import math

from leapfrogreturn import leapfrog

import sys
args=sys.argv
if(len(args)!=8):
    print('Error!')
    print('Usage: v0 thetadeg g m k rate fomula')
    exit()

v0=float(args[1])
thetadeg=float(args[2])
theta=thetadeg/360*2*3.14
g=float(args[3])
m=float(args[4])
k=float(args[5])
rate=float(args[6])
formula=args[7]

ret=leapfrog(v0,thetadeg,g,m,k,rate,formula,'result',True)

print('t:',ret['t'])
print('x:',ret['x'])

