#! /usr/local/bin/python3

import matplotlib.pyplot as plt
from ordinals2 import *

def init():
    plt.axes().set_aspect('equal')#, 'datalim')

def plot():
    ords = getOrds(size=12, lim=www)
    ticks = [o.slog for o in ords]
    labels = [str(o) for o in ords]
    plt.xticks(ticks=ticks, labels="")#labels, rotation=270)
    plt.yticks(ticks=ticks, labels=labels)

    xs = [x.slog for x in ords]
    ys = [x.slog for x in ords]
    plt.scatter(xs, ys, 1)

    # plt.xlabel('time (s)')
    # plt.ylabel('voltage (mV)')
    # plt.title('About as simple as it gets, folks')
    # plt.grid(True)    # cool
    plt.savefig("out.png")
    plt.show()


if __name__ == "__main__":
    init()
    plot()