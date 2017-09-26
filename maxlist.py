#coding=utf-8
import math

import sys
args=sys.argv
if(len(args)!=11):
    print('Usage: v0 g m k accuracy vartype minval maxval rate2 foldername')
    exit()

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from maxtheta import maxtheta

import os

v0=float(args[1])
g=float(args[2])
m=float(args[3])
k=float(args[4])
accuracy=float(args[5])

vartype=args[6]
minval=float(args[7])
maxval=float(args[8])
rate2=int(args[9])
foldername=args[10]

df=pd.DataFrame(columns=['v0','g','m','k','accuracy','maxtheta'])

for i in range(rate2):
    if vartype=='v0':
        v0=minval+(maxval-minval)/rate2*i
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
    
    ret=maxtheta(v0,g,m,k,accuracy)
    
    df2=pd.DataFrame([[v0,g,m,k,accuracy,ret]],columns=['v0','g','m','k','accuracy','maxtheta'])
    df=df.append(df2)
    
df.to_csv('maxtheta/'+foldername+'.csv',index=False)
