def fr(x):
    """Return the min digit of x.

    >>> min_digit(10)
    0
    >>> min_digit(4224)
    2
    >>> min_digit(1234567890)
    0
    >>> # make sure that you are using return rather than print
    >>> a = min_digit(123)
    >>> a
    1
    """
    x = str(x)
    i = 0
    r = x.count(str(i))
    ans = 0
    while r==0:
        i = i + 1
        r = x.count(str(i))
        ans = ans + 1
    return ans