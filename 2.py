import matplotlib.pyplot as plt
import numpy

def DecaySimulator(N,a,T):                 #gives the no of decays per experiment
    N_0=N
    t=0
    while t<T:                             #for each set of 10 sec  
        prob=numpy.random.random(N)
        sum=0
        for p in prob:
            if p>(10*a):                   #Since we are stimulating taking readings for 10 sec
                sum+=1
        N=sum
        t=t+10
    Decays=N_0-N                           #Decays per experiment   
    return Decays

def lister(N,a,T):                         #Runs the simulator 1000 times and stores the result in a list
    dec=[]
    for i in range(1000):
        dec.append(DecaySimulator(N,a,T))   
    return dec 

def counter(k:list):                       #Counts the frequency of each value(no of decays every 300 sec)
    decset=set(k)
    declist=list(decset)                   #Gives a list of all accuring values in the lsit
    x=[]
    y=[]
    for dec in declist:                    #frequency-value pair generator
        x.append(dec)
        count=0
        for elem in k:
            if elem==dec:
                count+=1
        y.append(count)
    return [x,y]


surv1=lister(500,0.00004,100)
surv2=lister(500,0.00002,100)
#print(surv1)

plt.plot(counter(surv1)[0],counter(surv1)[1])
plt.hist(surv1)
plt.xlabel("Total decay -100s-->")
plt.ylabel("Repeats-->")
plt.title("alpha=0.00004,N=500")
plt.show()

plt.plot(counter(surv2)[0],counter(surv2)[1])
plt.hist(surv2)
plt.xlabel("Total decay -100s-->")
plt.ylabel("Repeats-->")
plt.title("alpha=0.00002,N=500")
plt.show()
