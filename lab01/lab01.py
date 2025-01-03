from multiprocessing.connection import answer_challenge
from operator import truediv


def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 == 1 and b % 2 == 1
    


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    N = int(n)
    NN = N + 1
    ans = 1
    for x in range(1,NN):
        ans = ans * x
    return ans


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    if a+b>c and a+c>b and b+c>a:
        print('True')
    else:
        print('False')


def number_of_nine(n):
    """Return the number of 9 in each digit of a positive integer n.

    >>> number_of_nine(999)
    3
    >>> number_of_nine(9876543)
    1
    """
    N = str(n)
    ans = N.count('9')
    return ans



def min_digit(x):
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
   

