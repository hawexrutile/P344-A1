import matplotlib.pyplot as plt
import numpy as np

def DistFunction(u):
    return(np.arctan(np.sqrt(0.5)*np.tan((u-1)*np.pi)))

DistFunction(0)
N=np.random.rand(10000)
def Func1(th):
    return(1/(np.sin(th)**2+0.5*np.cos(th)**2))

fig,ax1=plt.subplots()
Y=DistFunction(np.random.rand(10000))
for i in range(10000):
    if Y[i]<0:
        Y[i]=Y[i]+np.pi
X=np.arange(0,3,0.01)

Curve=Func1(X)
ax1.hist(Y,edgecolor='black',bins=20)
ax1.set_xlabel('occurances')
ax1.set_ylabel('Distribution')
ax2=ax1.twinx()
ax2.plot(X,Curve,linestyle='-',color='red')
ax2.set_ylim(0,2.2)
ax2.set_ylabel('Given function')
plt.show()


U1= np.random.rand(10000)
U2= np.random.rand(10000)
Y=[]
for i in range(10000):
    if Func1(np.pi*U1[i])>=U2[i]*2.25:
        Y.append(np.pi*U1[i])
fig,ax1=plt.subplots()
ax1.hist(Y,edgecolor='black',bins=20)
ax1.set_xlabel('occurances')
ax1.set_ylabel('Distribution')
ax2=ax1.twinx()
X=np.arange(0,3.05,0.01)
Curve=Func1(X)
ax2.plot(X,Curve,linestyle='-',color='red')
ax2.set_ylim(0,2.2)
ax2.set_ylabel('Given function')
plt.show()