#coding=utf-8
def bisection(v0,thetadeg,g,m,k,accuracy):
    import math

    theta=thetadeg/360*2*3.14

    
    A=(m*g+k*v0*math.sin(theta))/(k*v0*math.cos(theta))
    B=m*m*g/(k*k)
    C=k/(m*v0*math.cos(theta))
    
    def f(x):
        return(A*x+B*math.log(1-C*x))

    def df(x):
        return(A-B*C/(1-C*x))
    
    ratio=0
    def div(a,b):
        return((a+b*ratio)/(ratio+1))
        
    flag=True
    
    while flag:
        ratio+=1
        flag=False
        a=(A-B*C)/(C*A)
        b=m/g*v0*math.cos(theta)
        
        while(abs(a-b)>=accuracy):
            if(f(a)*f(div(a,b))<=0):
                b=div(a,b)
            else:
                a=div(a,b)
            if(1-C*div(a,b)<=0):
                Flag=True
                break
    if(ratio!=1):
        print(ratio)
    return(a)
