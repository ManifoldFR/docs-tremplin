import matplotlib.pyplot as plt
import numpy as np

def suite(z0,a,N,filename="default"):
    res = [z0]
    for i in range(1,N+1):
        res.append(a*res[-1])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(np.real(res), np.imag(res),'r.--')
    ax.grid(True)
    ax.set_aspect('equal')
    fig.show()
    fig.savefig(filename+".png")
    fig.savefig(filename+".pdf")

suite(1,np.exp(1j*1.3),30,"notperiodico")
