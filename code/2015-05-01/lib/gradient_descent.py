import sympy as s
from sympy.interactive.printing import init_printing
from sympy.matrices import Matrix
import numpy as np

init_printing(use_unicode=False, wrap_line=False, no_global=True)

# In [1]: %load_ext autoreload
#
# In [2]: %autoreload 2

class GradientDescentState(object):
    """holds the state for gradient descent"""

    def __init__(self, size, symbols, fn, initalGuess, grad):
        self.numberOfVariables = size
        self.x = symbols
        self.fn = fn
        self.initalGuess = initalGuess
        self.grad = grad

        self.currentIterValue = Matrix(initalGuess)

    # compute the gradient at point
    def atPoint(self, subs):
        if len(subs) != self.numberOfVariables:
            raise Exception('airity mismatch: atPoint')

        res = self.grad
        for idx in range(0, self.numberOfVariables):
            res = res.subs(self.x[idx], subs[idx]);

        return res

    # one iteration of gradient descent
    def Next(self, step):

        # evaluate the gradinant at the current point
        gradAtPoint = self.atPoint(self.currentIterValue)

        # the new current point becomes the old current point
        # minus the gradient (at the point) times some scale factor
        self.currentIterValue = self.currentIterValue - (step * gradAtPoint)

        return self.currentIterValue


class Context(object):
    """some context where variables exists"""
    def __init__(self, size):
        self.numberOfVariables = size
        self.x = s.symbols('x:'+str(size))
        self.fn = None
        self.grad = None

    def setFn(self, expression):
        self.fn = expression

    def getGradient(self):
        if self.grad == None:

            derivs = []
            for idx in range(0, self.numberOfVariables):
                derivs.append(s.diff(self.fn, self.x[idx]))

            self.grad = Matrix(derivs)

        return self.grad

    def getGradDescentObject(self, initialGuess):
        return GradientDescentState(
                self.numberOfVariables,
                self.x,
                self.fn,
                initialGuess,
                self.getGradient())


