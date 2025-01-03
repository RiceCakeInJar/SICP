def f(x) :
    i = 1
    while x>1:
        if x % 2 ==0:
            print(x)
            x = x//2
            i = i + 1
        else:
            print(x)
            x = 3*x+1
            i = i + 1
    print('1')
    return i