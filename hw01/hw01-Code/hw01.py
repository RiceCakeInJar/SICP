""" Homework 1: Variables & Functions, Control """

from operator import add, sub, mul, neg

def a_sub_abs_b(a, b):
    """Return a-abs(b), but without calling abs.

    >>> a_sub_abs_b(2, 3)
    -1
    >>> a_sub_abs_b(2, -3)
    -1
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_sub_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = sub
    else:
        h = add
    return h(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two largest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # and a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return x*x+y*y+z*z-min(x,y,z)*min(x,y,z)

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    r = x - 1
    t = x % r
    while t > 0:
        r = r - 1
        t = x % r
    return r



def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return False

def t():
    print('1')

def f():
    print('2')

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    i = 1
    while x>1:
        if x % 2 ==0:
            print(round(x))
            x = x/2
            i = i + 1
        else:
            print(round(x))
            x = 3*x+1
            i = i + 1
    print('1')
    return i

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    else:
        i = 1
        o = n-1
        while i < k:
            n = n*o
            i = i + 1
            o = o - 1
        return n


def double_ones(n):
    """Return true if n has two ones in a row.
    
    >>> double_ones(1)
    False
    >>> double_ones(11)
    True
    >>> double_ones(2112)
    True
    >>> double_ones(110011)
    True
    >>> double_ones(12345)
    False
    >>> double_ones(10101010)
    False
    """
    n = str(n)
    i = n.count('11')
    if i >= 1:
        return True
    else:
        return False
    