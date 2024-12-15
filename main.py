from string import ascii_lowercase as letters
from sympy.parsing.sympy_parser import parse_expr
import inspect


def math_parsed(expr, context=None):
    if context is None:
        context = inspect.currentframe().f_back.f_locals
    return parse_expr(expr, transformations="all", local_dict=context)


def divisors(n, start=None, stop=None):
    for i in range(start or 1, int(stop or n)+1):
        if n % i == 0:
            yield i

def divisors_ls(n, start=None, stop=None):
    return list(divisors(n, start, stop))


def x_special(x):
    t = 2*x
    return [
        {int(n+k+1) for k in range(r)}
        for r in divisors(t, 2, t**.5)
        if (n:=(t-r*r-r)/r/2).is_integer()
    ]



def base_polynomial(degree, coeffs=None, **kwargs):
    if kwargs:
        coeffs = dict(kwargs)
    if not isinstance(coeffs, dict):
        coeffs = zip(letters, coeffs or [])
    return math_parsed("+".join(f"{letters[k]}x**{degree-k}" for k in range(degree+1)), context={}).subs(coeffs)
