from matplotlib           import pyplot as plt
from matplotlib           import cm
from mpl_toolkits.mplot3d import Axes3D

import mpl_toolkits.mplot3d.art3d   as Art3D
import arrow3d                      as arrow3d
import numpy                        as np


class plot3d(object):
    """encapsulates a plot in euclidian space"""
    def __init__(self, xlim, ylim, zlim):
        self.xlimMin           = xlim[0]
        self.xlimMax           = xlim[1]

        self.ylimMin           = ylim[0]
        self.ylimMax           = ylim[1]

        self.zlimMin           = zlim[0]
        self.zlimMax           = zlim[1]

        self.fig            = plt.figure(figsize=(15,15))
        self.ax             = None
        self.plottedObjects = []

        self.initPlot()
        self.initAxis()

    def initPlot(self):

        plt.title('plot')

        plt.ion()
        plt.draw()
        plt.show()

    def initAxis(self):
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.ax.set_xlim(self.xlimMin,self.xlimMax)
        self.ax.set_ylim(self.ylimMin,self.ylimMax)
        self.ax.set_zlim(self.zlimMin,self.zlimMax)

        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')

        plt.draw()

    def addSurface(self, fn, boxMin=-1.0, boxMax=1.0, step=0.1, color='r', lw=3, text=None):

        x = y = np.arange(boxMin, boxMax, step)
        X, Y = np.meshgrid(x, y)
        zs = np.array([fn(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
        Z = zs.reshape(X.shape)

        Gx, Gy = np.gradient(Z) # gradients with respect to x and y
        G = (Gx**2+Gy**2)**.5  # gradient magnitude
        N = G/G.max()  # normalize 0..1

        self.ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
            facecolors=cm.jet(N),
            linewidth=0, antialiased=False, shade=False)

        plt.draw()

        return 'ok'


    def clear(self):
        self.plottedObjects = []
        self.fig.delaxes(self.ax)
        self.initAxis()
        plt.draw()

