import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import sys

# Suite u_n
def u(n):
    return n*(np.sin(n*np.pi/2)+1)


# Fonction pour afficher un graphe de la suite entre les entiers a et N
def graphe(a,N):
    res = []
    abscisses = list(range(a,N+1))
    for i in range(a,N+1):
        res.append(u(i))

    fig = plt.figure()
    ax = plt.subplot(111)
    ax.grid(True)
    ax.plot(abscisses,res, 'r.--')
    ax.plot(abscisses,2*np.array(abscisses),'b.')
    ax.plot(abscisses,0*np.array(abscisses),'b.')

    ax.set_xlabel("n")
    ax.set_ylabel("un")

    epsBar = Line2D([0,1],[0,1],linewidth=1,figure=fig)

    fig.savefig("exemple.pdf")
    fig.savefig("exemple.png")
    fig.show()

if __name__ == "__main__":
    print(sys.argv)
    graphe(int(sys.argv[1]),int(sys.argv[2]))
