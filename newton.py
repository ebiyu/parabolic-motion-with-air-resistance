#coding=utf-8
def newton(v0,thetadeg,g,m,k,accuracy):
    import math

    theta=thetadeg/360*2*3.14

    
    A=(m*g+k*v0*math.sin(theta))/(k*v0*math.cos(theta))
    B=m*m*g/(k*k)
    C=k/(m*v0*math.cos(theta))
    
    def f(x):
        return(A*x+B*math.log(1-C*x))

    def df(x):
        return(A-B*C/(1-C*x))
    
    x2=m/k*v0*math.cos(theta)-accuracy
    x=0
    
    while(abs(x-x2)>=accuracy):
        x=x2
        x2=x-f(x)/df(x)
    
    return(x)
