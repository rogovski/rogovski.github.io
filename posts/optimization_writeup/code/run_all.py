import numpy as np
import lib.sim_anneal as sa

def Ackley(x,y):
    expinner =  -2.0 * np.sqrt(0.5 * (x**2 + y**2))
    expinner2 = 0.5 * (np.cos(2.0 * np.pi * x) + np.cos(2.0 * np.pi * y))
    return -20.0 * np.exp(expinner) - np.exp(expinner2) + np.e + 20.0


def runAckleySimAnneal(its):
    fsr = lambda(x): Ackley(x[0], x[1])
    conf = sa.AnnealConfig(-10.0, 10.0, its)
    return sa.SimAnneal(conf, fsr)


def SimpleRidge(x,y):
    return (0.5 - x ** 2 + y ** 2) * (np.exp( 1 - x**2 - y**2 ))


def runSimpleRidgeSimAnneal(its):
    fsr = lambda(x): SimpleRidge(x[0], x[1])
    conf = sa.AnnealConfig(-3.0, 3.0, its)
    return sa.SimAnneal(conf, fsr)


def beale(x,y):
    return ((1.5 - x + x*y)**2.0) + ((2.25 - x + x*y**2.0)**2.0) + ((2.625 - x + x*y**3.0)**2.0)


def runBealeSimAnneal(its):
    fsr = lambda(x): beale(x[0], x[1])
    conf = sa.AnnealConfig(-4.5, 4.5, its)
    return sa.SimAnneal(conf, fsr)