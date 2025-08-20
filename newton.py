import numpy as np

# Directions:
# accept a starting value, and the function, , to optimize
# implement the iterative algorithm
# implement the stopping criterion (feel free to keep this simple)
# calculate the first and second derivatives using a basic finite difference approach to estimating the derivative based on the definition of a derivative as a limit
# note that the second derivative can be seen as calling the first derivative twice…


def first_derivative(func, x):
    """Return the first derivate of a given function"""
    return (func(x + np.finfo(float).eps) - func(x)) / np.finfo(float).eps


def second_derivative(first, x):
    """Return the second derivate of a given function based on the provided first derivative"""
    return (first(x + np.finfo(float).eps) - first(x)) / np.finfo(float).eps


def newtonsMethod(start, fx, end):
    """Implement Newton's Method for optimization."""
    t = start
    for i in range(start, end):
        first_der = first_derivative(fx, t - 1)
        second_der = second_derivative(first_der, t - 1)
        xt = (t - 1) - first_der / second_der
        t += 1
        if abs(xt - t) < np.finfo(float).eps:
            return t
