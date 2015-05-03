import numpy as np
import lib.plot3d as plt
import sympy as s
import lib.gradient_descent as gd

def holder(x,y):
    sqinner = np.sqrt(x**2 + y**2)
    expinner = np.abs(1 - (sqinner / np.pi))
    return - np.abs( np.sin(x) * np.cos(y) * np.exp( expinner ) )


def plotHolder():
    p = plt.plot3d([-10.0,10.0],[-10.0,10.0],[-20.0,1.0])
    p.addSurface(holder, boxMin=-10.0, boxMax=10.0)