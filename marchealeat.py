import random
from matplotlib import pyplot as plt
from time import *

def deplac(p):
    c = random.random()
    return int(c <= p)*2 - 1

def marche(n):
    res = [0]
    for _ in range(1,n):
        res.append(res[-1] + deplac(0.5))
    return res

def graphe(n):
    X = list(range(n))
    Y = marche(n)
    fig = plt.Figure(figsize=(6,4))
    ax = fig.add_subplot(111)
    ax.plot(X,Y)
    ax.set_xlabel("Temps t")
    ax.set_ylabel("Position Xt")
    ax.grid()
    canvas = plt.FigureCanvasBase(figure=fig)
    canvas.print_figure("marcheJM.png",dpi=100)

if __name__ == "__main__":
    graphe(2000)
