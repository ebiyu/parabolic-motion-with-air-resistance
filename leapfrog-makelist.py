#coding=utf-8
import math

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from leapfrogreturn import leapfrog

import sys
args=sys.argv
if(len(args)!=11):
    print('Error!')
    print('Usage: v0 thetadeg g m k rate vartype minval maxval int')
    exit()

v0=float(args[1])
thetadeg=float(args[2])
g=float(args[3])
m=float(args[4])
k=float(args[5])
rate=float(args[6])

vartype=args[7]
minval=float(args[8])
maxval=float(args[9])
rate2=int(args[10])

filename=input('filename>')

df=pd.DataFrame(columns=['v0','thetadeg','g','m','k','rate','t','x','y','vx','vy','ax','ay'])

for i in range(rate2):
    if vartype=='v0':
        v0=minval+(maxval-minval)/rate2*i
    elif vartype=='thetadeg':
        thetadeg=minval+(maxval-minval)/rate2*i
    elif vartype=='g':
        g=minval+(maxval-minval)/rate2*i
    elif vartype=='m':
        m=minval+(maxval-minval)/rate2*i
    elif vartype=='k':
        k=minval+(maxval-minval)/rate2*i
    elif vartype=='rate':
        rate=minval+(maxval-minval)/rate2*i
    else:
        print('Eroor!')
        exit()
    
    ret=leapfrog(v0,thetadeg,g,m,k,rate)
    
    df2=pd.DataFrame([[v0,thetadeg,g,m,k,rate,ret['t'],ret['x'],ret['y'],ret['vx'],ret['vy'],ret['ax'],ret['ay']]],columns=['v0','thetadeg','g','m','k','rate','t','x','y','vx','vy','ax','ay'])
    df=df.append(df2)
    
df.to_csv('list/'+filename+'.csv',index=False)
