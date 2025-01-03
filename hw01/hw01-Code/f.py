def f(x):
    r = x - 1
    t = x % r
    while t > 0:
        r = r - 1
        t = x % r
    return r
