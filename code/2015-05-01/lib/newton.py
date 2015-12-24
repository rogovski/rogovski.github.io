import sympy as s
from sympy.interactive.printing import init_printing
from sympy.matrices import Matrix

init_printing(use_unicode=False, wrap_line=False, no_global=True)

# In [1]: %load_ext autoreload
#
# In [2]: %autoreload 2

class NewtonState(object):
    """holds the state for newtons method"""

    def __init__(self, size, symbols, fnList, initalGuess, jInv):
        self.numberOfVariables = size
        self.x = symbols
        self.fn = fnList
        self.initalGuess = initalGuess
        self.jacobiInv = jInv

        self.currentIterValue = Matrix(initalGuess)
        self.AggFn = Matrix(fnList.values())

    def F(self, subs):
        if len(subs) != self.numberOfVariables:
            raise Exception('airity mismatch: F')

        fRes = self.AggFn
        for idx in range(0, self.numberOfVariables):
            fRes = fRes.subs(self.x[idx], subs[idx]);

        return fRes

    def JF(self, subs):
        if len(subs) != self.numberOfVariables:
            raise Exception('airity mismatch: JF')

        jfRes = self.jacobiInv
        for idx in range(0, self.numberOfVariables):
            jfRes = jfRes.subs(self.x[idx], subs[idx]);

        return jfRes

    def Next(self):
        a = self.currentIterValue
        fAta = self.F(a)
        jfAta = self.JF(a)

        self.currentIterValue = (a - (jfAta * fAta)).evalf()

        return self.currentIterValue

class Context(object):
    """some context where variables exists"""
    def __init__(self, size):
        self.numberOfVariables = size
        self.x = s.symbols('x:'+str(size))
        self.fn = {}
        self.jacobi = None
        self.jacobiInv = None

    def addFn(self, name, expression):
        self.fn[name] = expression

    def removeFn(self, name):
        del self.fn[name]

    def getJacobi(self):
        if self.jacobi == None:
            outer = []
            for k, v in self.fn.iteritems():
                inner = []
                for idx in range(0, self.numberOfVariables):
                    inner.append(s.diff(v, self.x[idx]))
                outer.append(inner)

            self.jacobi = Matrix(outer)

        return self.jacobi

    def getJacobiInv(self):
        if self.jacobiInv == None:
            self.jacobiInv = self.getJacobi().inv()

        return self.jacobiInv

    def getNewton(self, initialGuess):
        return NewtonState(
                self.numberOfVariables,
                self.x,
                self.fn,
                initialGuess,
                self.getJacobiInv())

# | task is to solve this system of equations
# a) x^2 + y^2 - 10 = 0
# b) 2x  + y   - 1  = 0

c = Context(2);

# c.addFn('f1', c.x[0]**2 + c.x[1]**2 - 10)
# c.addFn('f2', 2 * c.x[0] + c.x[1] - 1)

# c.addFn('f1', c.x[0])
# c.addFn('f2', s.exp(1 - c.x[0]**2 - c.x[1]**2))

c.addFn('f1', c.x[0])
c.addFn('f2', 1 + 2 * (c.x[0]**2) - 2 * (c.x[1]**2))