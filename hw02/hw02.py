""" Homework 2: Higher-Order Functions"""


from operator import add, mul, sub

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1


#####################
# Required Problems #
#####################


def compose(h, g):
    """Return a function f, such that f(x) = h(g(x)).

    >>> compose(square, triple)(5)
    225
    >>> double_inc = compose(increment, increment)
    >>> double_inc(3)
    5
    >>> double_inc(4)
    6
    """
    def ans(x):
        return h(g(x))
    return ans

def product(n, f):
    """Return the product of the first n terms in a sequence.
    n -- a positive integer
    f -- a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    i = 1
    s = 1
    while i<= n:
        s *= f(i)
        i += 1
    return s


def accumulate(combiner, base, n, f):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are f(1), f(2), ..., f(n).  combiner is a
    two-argument commutative, associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    i = 1
    s = base
    while i <= n:
        s = combiner(s,f(i))
        i += 1
    return s


def summation_using_accumulate(n, f):
    """Returns the sum of f(1) + ... + f(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check('hw02.py', 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(add,0,n,f)


def product_using_accumulate(n, f):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> # ban iteration and recursion
    >>> check('hw02.py', 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    return accumulate(mul,1,n,f)


def missions(f):
    """DO NOT EDIT THIS FUNCTION"""
    def mission1(f):
        if f(0) == 0 and f(1) == 2:
            print('MISSION 1 SOLVED')
            return lambda g: mission2(g(f))
        else:
            print('MISSION 1 FAILED')

    def mission2(f):
        if f(0) == 0 and f(1) == 2:
            print('MISSION 2 SOLVED')
            return mission3(0, 0)
        else:
            print('MISSION 2 FAILED')

    def mission3(f, g):
        def mission3_inner(f):
            if f == g:
                return mission3(f, g + 1)

        if g == 5:
            print('MISSION 3 SOLVED')
            return 'The cake is a lie.'
        else:
            return mission3_inner

    return mission1(f)


def get_the_cake(missions):
    """
    Write a higher order function so that it calls three
    mission functions in turn and return the hidden cake.
    You are not allowed to return variable cake or print
    the messages directly. A correct solution contains
    only one expression.

    By the way, do you know that "The cake is a lie" is 
    a catchphrase from the 2007 video game Portal? Visit
    https://en.wikipedia.org/wiki/The_cake_is_a_lie
    if you have never played Portal before!

    >>> the_cake = get_the_cake(missions)
    MISSION 1 SOLVED
    MISSION 2 SOLVED
    MISSION 3 SOLVED
    >>> the_cake
    'The cake is a lie.'
    >>> # check that your answer consists of nothing but an
    >>> # expression (this docstring) and a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(get_the_cake)).body[0].body]
    ['Expr', 'Return']
    """
    return missions(lambda x:x*2)(lambda x:x)(0)(1)(2)(3)(4)

def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love NJU", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love NJU
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """
    def my_secret(password_attempt,i=1):
        if i<=num_attempts:
            if password_attempt == password:
                print(secret)
            else:
                print('INCORRECT PASSWORD')
                i += 1
        else:
            print('SECRET LOCKED')
            i += 1
        return lambda x:my_secret(x,i)
    return my_secret
    


##########################
# Just for fun Questions #
##########################


def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"


three = successor(two)


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.
    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
