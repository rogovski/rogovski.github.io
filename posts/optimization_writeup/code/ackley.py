import numpy as np
import lib.plot3d as plt
import sympy as s
import lib.gradient_descent as gd
import lib.sim_anneal as sa


def Ackley(x,y):
    expinner =  -2.0 * np.sqrt(0.5 * (x**2 + y**2))
    expinner2 = 0.5 * (np.cos(2.0 * np.pi * x) + np.cos(2.0 * np.pi * y))
    return -20.0 * np.exp(expinner) - np.exp(expinner2) + np.e + 20.0


def plotAckley():
    p = plt.plot3d([-10.0, 10.0],[-10.0, 10.0],[0.0, 25.0])
    p.addSurface(Ackley, boxMin=-10.0, boxMax=10.0)


def runSimAnneal(its):
    fsr = lambda(x): Ackley(x[0], x[1])
    conf = sa.AnnealConfig(-10.0, 10.0, its)
    return sa.SimAnneal(conf, fsr)