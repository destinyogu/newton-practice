import numpy as np
from scipy.differentiate import hessian

def deriv1(f, x, eps = 1e-6):
    """Return the gradient vector (the first derivative)."""
    return np.gradient(f(x), eps)
    
def deriv2(f, x):
    """Return the Hessian matrix (the second derivative with respect to all pairs of elements of x."""
    return hessian(f, x)
    
def multivariate(fx, start, tol = 1e-3):
    """Implement Newton's Method for optimization."""
    start_new = start - np.linalg.inv(deriv2(fx, start)) * deriv1(fx, start)
    t = start_new
    while abs(start_new - t) < tol:
        xt = start_new
        start_new = xt - np.linalg.inv(deriv2(fx, xt)) * deriv1(fx, xt) 
    return start_new, fx(start_new)