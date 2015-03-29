import sympy as s


# In [1]: %load_ext autoreload
#
# In [2]: %autoreload 2

x, y = s.symbols('x y')

expr_f = (0.5 - x ** 2 + y ** 2) * (s.exp( 1 - x**2 - y**2 ))

expr_fx = s.diff(expr_f, x)
expr_fy = s.diff(expr_f, y)
expr_fxx = s.diff(expr_fx, x)
expr_fyy = s.diff(expr_fy, y)
expr_fxy = s.diff(expr_fx, y)


def EvalAt(a,b):
    return expr_f.subs(x,a).subs(y,b)


def Eval_fxx(a,b):
    return expr_fxx.subs(x,a).subs(y,b)


def SecondPartialTest(a,b):
    prodLeft = (expr_fxx.subs(x,a)).subs(y,b)
    prodRight = (expr_fyy.subs(x,a)).subs(y,b)
    subtractRight = ((expr_fxy.subs(x,a)).subs(y,b)) ** 2
    return prodRight*prodLeft - subtractRight


def spt(a,b):
    prodLeft = (expr_fxx.subs(x,a)).subs(y,b)
    prodRight = (expr_fyy.subs(x,a)).subs(y,b)
    subtractRight = ((expr_fxy.subs(x,a)).subs(y,b)) ** 2
    dVal = prodRight*prodLeft - subtractRight


    if (dVal.evalf() == 0):
        return "Inconclusive at (" + str(a) + ", " + str(b) + ")"

    elif ( dVal.evalf() < 0 ):
        return "Saddle Point at (" + str(a) + ", " + str(b) + ")"

    elif ( dVal.evalf() > 0 and prodLeft.evalf() > 0 ):
        return "Relative Minimum at (" + str(a) + ", " + str(b) + ")"

    elif ( dVal.evalf() > 0 and prodLeft.evalf() < 0 ):
        return "Relative Maximum at (" + str(a) + ", " + str(b) + ")"

    else:
        return "unreachable"

