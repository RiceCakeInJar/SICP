""" Homework 5: Nonlocal and Generators"""

from ADT import tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    password_tried=[]#用于储存已经尝试过的密码
    def withdraw(money,password_try):
        nonlocal balance,password_tried,password
        if len(password_tried)==3:#验证是否试错3次
            return 'Your account is locked. Attempts: {0}'.format(password_tried)
        if password_try!=password:
            password_tried.append(password_try)#将试错的密码添加到试错列表中
            return 'Incorrect password'
        if money>balance:
            return 'Insufficient funds'
        balance-=money
        return balance
    return withdraw


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    password_box=[]
    if old_pass not in password_box:
        try_get=withdraw(0,old_pass)
        if type(try_get)==str:
            return try_get
        password_box.extend([old_pass,new_pass])
    if old_pass in password_box:
        password_box.append(new_pass)
        return lambda x,y:withdraw(x,password_box[0]) if y in password_box else withdraw(x,y)


def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of all elements in seq. The permutations could be yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    #对一个seq，抽出头元素，将剩下的seq0全排列，再将头元素插入到每种seq0排列的每个空位
    seq = list(seq)
    if len(seq)==1 or seq==[]:
        yield seq#单元素直接输出
    else:
        for z in permutations(seq[1:]):#遍历seq0的每一种排列，z是seq0的一种排列：seq1
            for y in range(len(seq)):#y用来标记头位元素插入的位置，从头到尾，在seq1的每个间隙位置插入一次
                yield z[:y]+[seq[0]]+z[y:]

def two_sum_pairs(target, pairs):
    """Return True if there is a pair in pairs that sum to target.
    """
    for (i, j) in pairs:
        if i + j == target:
            return True
    return False

def pairs(lst):
    """Yield the search space for two_sum_pairs. 

    >>> two_sum_pairs(1, pairs([1, 3, 3, 4, 4])) 
    False
    >>> two_sum_pairs(8, pairs([1, 3, 3, 4, 4])) 
    True
    >>> lst = [1, 3, 3, 4, 4]
    >>> plst = pairs(lst)
    >>> n, pn = len(lst), len(list(plst))
    >>> n * (n - 1) / 2 == pn
    True
    """
    "*** YOUR CODE HERE ***"
    for x in range(len(lst)-1):
        for y in range(x+1,len(lst)):
            yield lst[x],lst[y]

def two_sum_list(target, lst):
    """Return True if there are two different elements in lst that sum to target.

    >>> two_sum_list(1, [1, 3, 3, 4, 4]) 
    False
    >>> two_sum_list(8, [1, 3, 3, 4, 4]) 
    True
    """
    visited = lst
    for val in lst:
        visited.pop(0)
        if target-val in visited:
            return True
    return False

def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> k = tree(5, [tree(7, [tree(2)]), tree(8, [tree(3), tree(4)]), tree(5, [tree(4), tree(2)])])
    >>> v = tree('Go', [tree('C', [tree('C')]), tree('A', [tree('S'), tree(6)]), tree('L', [tree(1), tree('A')])])
    >>> type(lookups(k, 4))
    <class 'generator'>
    >>> sorted([f(v) for f in lookups(k, 2)])
    ['A', 'C']
    >>> sorted([f(v) for f in lookups(k, 3)])
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    "*** YOUR CODE HERE ***"
    def display(tree):
        displayed_tree = [label(tree)]
        if is_leaf(tree):
            return displayed_tree
        for x in branches(tree):
            displayed_tree+=display(x)
        return displayed_tree
    displayed_k,index_list=display(k),[]
    for y in displayed_k:
        if y==key:
            index_list.append(displayed_k.index(y))
            displayed_k[displayed_k.index(y)]=None
    def evaluation(t):
        return lambda x:display(x)[t]
    yield from [evaluation(i)for i in index_list]

##########################
# Just for fun Questions #
##########################

def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
