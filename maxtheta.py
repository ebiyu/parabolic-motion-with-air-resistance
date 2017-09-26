#coding=utf-8
from bisection import bisection
def maxtheta(v0,g,m,k,accuracy):
    def f(x):
        return(bisection(v0,x,g,m,k,accuracy))
    
    def df(x):
        return((f(x+0.05)-f(x-0.05))/0.1)
        
    def div(a,b):
        return((a+b)/2)
        
    x=-1
    for theta in range(50):
        x2=x
        x=f(theta)
        
        if(x2>x):
            break
    
    return(theta-1);
