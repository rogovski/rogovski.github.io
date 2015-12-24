import numpy as np
import lib.plot3d as plt
import sympy as s
import lib.gradient_descent as gd

def SimpleEp(x,y):
    return x ** 2 + y ** 2

c = gd.Context(2);
c.setFn(c.x[0] ** 2 + c.x[1] ** 2)


def plotSimpleEp():
    p = plt.plot3d([-2.0, 2.0],[-2.0, 2.0],[0, 5.0])
    p.addSurface(SimpleEp, boxMin=-4.0, boxMax=4.0)