#coding=utf-8
from bisection import bisection
def maxtheta(v0,g,m,k,accuracy):
    def f(x):
        return(bisection(v0,x,g,m,k,accuracy))
    
    def df(x):
        return((f(x+0.05)-f(x-0.05))/0.1)
        
    def div(a,b):
        return((a+b)/2)
        
    a=0
    b=45
    
    while(abs(a-b)>=0.1):
        if(df(a)*df(div(a,b))<=0):
            b=div(a,b)
        else:
            a=div(a,b)
    return(a)
