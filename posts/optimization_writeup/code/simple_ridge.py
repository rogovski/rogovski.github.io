import numpy as np
import lib.plot3d as plt
import sympy as s
import lib.gradient_descent as gd
import lib.sim_anneal as sa

def SimpleRidge(x,y):
    return (0.5 - x ** 2 + y ** 2) * (np.exp( 1 - x**2 - y**2 ))


def plotSimpleRidge():
    p = plt.plot3d([-5.0, 5.0],[-5.0, 5.0],[-3.0, 3.0])
    p.addSurface(SimpleRidge, boxMin=-4.0, boxMax=4.0)


# @its: number of iterations to perform
def runSimAnneal(its):
    fsr = lambda(x): SimpleRidge(x[0], x[1])
    conf = sa.AnnealConfig(-3.0, 3.0, its)
    return sa.SimAnneal(conf, fsr)
