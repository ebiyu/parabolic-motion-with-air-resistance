#coding=utf-8
import math

import sys
args=sys.argv
if(len(args)!=13):
    print('Usage: v0 thetadeg g m k rate formula vartype minval maxval int foldername')
    exit()

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from leapfrogreturn import leapfrog

import os

v0=float(args[1])
thetadeg=float(args[2])
g=float(args[3])
m=float(args[4])
k=float(args[5])
rate=float(args[6])
formula=args[7]

vartype=args[8]
minval=float(args[9])
maxval=float(args[10])
rate2=int(args[11])
foldername=args[12]

os.mkdir(foldername)
os.mkdir(foldername+'/images')
os.mkdir(foldername+'/data')


df=pd.DataFrame(columns=['v0','thetadeg','g','m','k','rate','formula','t','x','y','vx','vy','ax','ay'])

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
    
    ret=leapfrog(v0,thetadeg,g,m,k,rate,formula,foldername)
    
    print(str(round((i+1)/rate2*100,1))+'%('+str(i)+'/'+str(rate2)+')'+vartype+'='+str(minval+(maxval-minval)/rate2*i))
    
    df2=pd.DataFrame([[v0,thetadeg,g,m,k,rate,formula,ret['t'],ret['x'],ret['y'],ret['vx'],ret['vy'],ret['ax'],ret['ay']]],columns=['v0','thetadeg','g','m','k','rate','formula','t','x','y','vx','vy','ax','ay'])
    df=df.append(df2)
    
df.to_csv(foldername+'/list.csv',index=False)
