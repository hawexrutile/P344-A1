import matplotlib.pyplot as plt
import numpy as np
import math
def survivors(N,a,T):
    pop=[]
    N_0=N
    x=0
    t=0
    while t<T:
        pop.append(N)
        prob=np.random.random(N)
    
        
        sum=0
        for p in prob:
            if p>a:
                sum=sum+1
        N=sum
        t=t+1
    x = np.linspace(0, t, 100)
    y = np.exp(x)
    return [range(t),pop,[N_0*np.exp(-a*i) for i in range(t)]]
      

        

surv1=survivors(100,0.01,300)
surv2=survivors(5000,0.03,300)

plt.plot(surv1[0],surv1[1])
plt.plot(surv1[0], surv1[2])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.01,N=100 Linear")
plt.show()

plt.plot(surv2[0],surv2[1])
plt.plot(surv2[0], surv2[2])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.03,N=5000 Linear")
plt.show()


plt.semilogy()
plt.plot(surv1[0],surv1[1])
plt.plot(surv1[0], surv1[2])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.01,N=100 Log")
plt.show()

plt.semilogy()
plt.plot(surv2[0],surv2[1])
plt.plot(surv2[0], surv2[2])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.03,N=5000 Log")
plt.show()
