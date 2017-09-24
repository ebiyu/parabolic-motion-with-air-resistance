#coding=utf-8
import math

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from newton import newton

import os

import sys
args=sys.argv
if(len(args)!=11):
    print('Error!')
    print('Usage: v0 thetadeg g m k accuracy vartype minval maxval rate2')
    exit()

v0=float(args[1])
thetadeg=float(args[2])
g=float(args[3])
m=float(args[4])
k=float(args[5])
accuracy=float(args[6])

vartype=args[7]
minval=float(args[8])
maxval=float(args[9])
rate2=int(args[10])

foldername=input('foldername>')
os.mkdir(foldername)

df=pd.DataFrame(columns=['v0','thetadeg','g','m','k','accuracy','x'])

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
    elif vartype=='accuracy':
        rate=accuracy+(maxval-minval)/rate2*i
    else:
        print('Eroor!')
        exit()
    
    ret=newton(v0,thetadeg,g,m,k,accuracy)
    
    df2=pd.DataFrame([[v0,thetadeg,g,m,k,accuracy,ret]],columns=['v0','thetadeg','g','m','k','accuracy','x'])
    df=df.append(df2)
    
df.to_csv(foldername+'/list.csv',index=False)
