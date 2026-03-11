def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    def grad_f(x):
        return 2*a*x+b

    for n in range(steps):
        x0=x0-lr*grad_f(x0)
    return x0
    pass