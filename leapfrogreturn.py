#coding=utf-8
def leapfrog(v0,thetadeg,g,m,k,rate,formula,folder,showgraph=False):
    import math

    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt

    theta=thetadeg/360*2*3.14

    t=0
    x=0
    y=0

    vx=v0*math.cos(theta)
    vy=v0*math.sin(theta)
    ax=0
    ay=0
    
    df=pd.DataFrame(columns=['t','x','y','vx','vy','ax','ay'])

    while(y>=0):
        vx+=ax/rate
        vy+=ay/rate
        
        if formula=='kv':
            ax=(-k*vx)/m
            ay=(-m*g-k*vy)/m
        else:
            ax=-k*vx*math.sqrt(vx*vx+vy*vy)/m
            ay=-k*vy*math.sqrt(vx*vx+vy*vy)/m-g
        
        x+=vx/rate
        y+=vy/rate
        
        t+=1/rate
        
        df2=pd.DataFrame([[t,x,y,vx,vy,ax,ay]],columns=['t','x','y','vx','vy','ax','ay'])
        df=df.append(df2)
        
    df.to_csv(folder+'/data/'+'v0'+str(v0)+'θ'+str(thetadeg)+'g'+str(g)+'m'+str(m)+'k'+str(k)+'rate'+str(rate)+' F='+formula+'.csv',index=False)
    df.plot.scatter(x='x',y='y')
    plt.axes().set_aspect('equal',adjustable='box')
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.title('v0:'+str(v0)+' ,θ:'+str(thetadeg)+' ,g:'+str(g)+' ,m:'+str(m)+' ,k:'+str(k)+' ,rate:'+str(rate)+' F='+formula)
    plt.savefig(folder+'/images/'+'v0'+str(v0)+'θ'+str(thetadeg)+'g'+str(g)+'m'+str(m)+'k'+str(k)+'rate'+str(rate)+' F='+formula+'.png')
    if(showgraph==True):
        plt.show()
    plt.close()

    return({'t':t,'x':x,'y':y,'vx':vx,'vy':vy,'ax':ax,'ay':ay})
