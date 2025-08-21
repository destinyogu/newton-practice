import numpy as np

#Directions:
# accept a starting value, and the function, , to optimize
#implement the iterative algorithm
#implement the stopping criterion (feel free to keep this simple)
#calculate the first and second derivatives using a basic finite difference approach to estimating the derivative based on the definition of a derivative as a limit
#note that the second derivative can be seen as calling the first derivative twice…

def first_derivative(func, x, eps = 1e-8):
    """Return the first derivate of a given function"""
    return (func(x + eps) - func(x))/ eps

def second_derivative(func, x, eps = 1e-5):
    """Return the second derivate of a given function based on the provided first derivative"""
    return (first_derivative(f, x+eps, eps) - first_derivative(f, x, eps))/ eps

def newtonsMethod(start, fx, end = 1e-4):
    """Implement Newton's Method for optimization."""
    start_new = start - first_derivative(fx, start) / seconda_derivative(fx, start)
    t = start_new
    while abs(start_new - t) < end:
        xt = start_new
        start_new = xt - first_derivative(fx, xt) / seconda_derivative(fx, xt)
    return x_new, f(start_new)
