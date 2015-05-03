import numpy as np
import lib.plot3d as plt
import sympy as s
import lib.gradient_descent as gd
import lib.sim_anneal as sa


def beale(x,y):
    return ((1.5 - x + x*y)**2.0) + ((2.25 - x + x*y**2.0)**2.0) + ((2.625 - x + x*y**3.0)**2.0)


def plotBeale():
    p = plt.plot3d([-4.5, 4.5], [-4.5, 4.5], [0, 4.5])
    p.addSurface(beale, boxMin=-4.5, boxMax=4.5)


def runSimAnneal(its):
    fsr = lambda(x): beale(x[0], x[1])
    conf = sa.AnnealConfig(-4.5, 4.5, its)
    return sa.SimAnneal(conf, fsr)