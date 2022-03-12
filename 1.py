import matplotlib.pyplot as plt
import numpy

def survivors(N,a,T):
    pop=[]
    x=0
    t=0
    while t<T:
        pop.append(N)
        prob=numpy.random.random(N)
        sum=0
        for p in prob:
            if p>a:
                sum=sum+1
        N=sum
        t=t+1
    return [range(t),pop]
      

        

surv1=survivors(500,0.00004,300)
surv2=survivors(5000,0.03,300)

plt.plot(surv1[0],surv1[1])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.01,N=100 Linear")
plt.show()

plt.plot(surv2[0],surv2[1])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.01,N=100 Linear")
plt.show()


plt.semilogy()
plt.plot(surv1[0],surv1[1])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.01,N=100 Linear")
plt.show()

plt.semilogy()
plt.plot(surv2[0],surv2[1])
plt.xlabel("t-->")
plt.ylabel("N-->")
plt.title("alpha=0.01,N=100 Linear")
plt.show()
