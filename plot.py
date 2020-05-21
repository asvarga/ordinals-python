#! /usr/local/bin/python3

import matplotlib.pyplot as plt
from ordinals2 import *

#### ####

FONTSIZE = 6
POINTSIZE = 1

#### ####

def init():
    plt.axes().set_aspect('equal')#, 'datalim')
    plt.gcf().set_size_inches(10, 10)
    # plt.title('title')
    # plt.grid(True)

def plot():
    ords = getOrds(size=14, lim=www)[1:] # size=12, lim=www
    xs = [x.slog for x in ords]
    ys = [x.nslog for x in ords]

    labels = [str(o) for o in ords]
    plt.xticks(ticks=xs,
               labels=labels,
               fontsize=FONTSIZE, rotation=270)
    plt.yticks(ticks=ys,
               labels=labels,
               fontsize=FONTSIZE)

    # plt.xlabel('xlabel')
    # plt.ylabel('ylabel')
    plt.scatter(xs, ys, s=POINTSIZE)
    plt.savefig("fig.png")
    plt.show()

#### ####

if __name__ == "__main__":
    init()
    plot()