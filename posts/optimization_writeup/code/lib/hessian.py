import sympy as s
from sympy.interactive.printing import init_printing
from sympy.matrices import Matrix

init_printing(use_unicode=False, wrap_line=False, no_global=True)

# In [1]: %load_ext autoreload
#
# In [2]: %autoreload 2

class Context(object):
	"""some context where variables exists"""
	def __init__(self, size):
		self.numberOfVariables = size
		self.x = s.symbols('x:'+str(size))
		self.fn = None
		self.hessian = None
		self.detHessian = None

	def setFn(self, expression):
		self.fn = expression

	def getHessian(self):

		expr = self.fn

		hessianRows = []
		for idx in range(0, self.numberOfVariables):

			hessianRow = []

			diffWrt = s.diff(expr, self.x[idx])

			for idx2ndDeriv in range(0, self.numberOfVariables):

				hessianRow.append(s.diff(diffWrt, self.x[idx2ndDeriv]))

			hessianRows.append(hessianRow)

		self.hessian = Matrix(hessianRows)

		return self.hessian

	# compute the determinate of the hessian at point [x1 .. xn]
	def detHessianAt(self, subs):

		if len(subs) != self.numberOfVariables:

			raise Exception('airity mismatch: detHessianAt')

		if self.hessian == None:

			self.hessian = self.getHessian()

		if self.detHessian == None:

			self.detHessian = self.hessian.det()

		detHessian = self.detHessian

		for idx in range(0, self.numberOfVariables):

			detHessian = detHessian.subs(self.x[idx], subs[idx]);

		return detHessian


	def secondPartialTest(self, subs):

		dValue = self.detHessianAt(subs).evalf()

		if(dValue < 0):

			return "Saddle Point at f(" + str(subs) + ")"

		if(dValue == 0):

			return "Inconclusive at f(" + str(subs) + ")"

		# get the function at the top left of the hession
		secondDerivAtSub = self.hessian[0,0]

		value = secondDerivAtSub

		for idx in range(0, self.numberOfVariables):

			value = value.subs(self.x[idx], subs[idx]);

		value = value.evalf()

		if value > 0:

			return "Relative Minimum at f(" + str(subs) + ")"

		if value < 0:

			return "Relative Maximum at f(" + str(subs) + ")"


c = Context(2)

# c.setFn((0.5 - c.x[0] ** 2 + c.x[1] ** 2) * (s.exp( 1 - c.x[0]**2 - c.x[1]**2 )))
c.setFn( ( - c.x[0]**3 ) + ( 4*c.x[0]*c.x[1] ) - ( 2 * ( c.x[1] ** 2 ) ) + 1 )
