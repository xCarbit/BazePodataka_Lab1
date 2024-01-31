import sympy
import numpy
x=sympy.Symbol('x')

f=sympy.pi-x
a=sympy.integrate(f,(x,0,+oo))
#v=a.subs(x,1)
print(a)
