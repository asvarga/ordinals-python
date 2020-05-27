#! /usr/local/bin/python3

import matplotlib.pyplot as plt
from ordinals import *

#### ####

FONTSIZE = 6
POINTSIZE = 1

#### ####

def init():
    plt.axes().set_aspect('equal')#, 'datalim')
    plt.gcf().set_size_inches(10, 10)
    plt.title('f(x) := x*x')
    # plt.grid(True)

def plot():

    ORDRANGE = True
    def f(x): return x*x

    xos = getOrds(size=12, inf=one, sup=www) # size=12, lim=www
    yos = [f(x) for x in xos]
    xs = [x.slog() for x in xos]
    ys = [y.slog() for y in yos] if ORDRANGE else yos

    xticks = xs
    xlabels = [str(o) for o in xos]

    yticks, ylabels = None, None
    if ORDRANGE:
        ally = getOrds(size=len(yos[-1].bp), inf=yos[0], sup=yos[-1])
        yticks = [y.slog() for y in ally]
        ylabels = [str(o) for o in ally]

    plt.xticks(ticks=xticks,
               labels=xlabels,
               fontsize=FONTSIZE, rotation=270)
    plt.yticks(ticks=yticks,
               labels=ylabels,
               fontsize=FONTSIZE)

    plt.scatter(xs, ys, s=POINTSIZE)
    plt.savefig("fig.png")
    plt.show()

#### ####

if __name__ == "__main__":
    init()
    plot()