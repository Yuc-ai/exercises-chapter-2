def isprime(n):
    from math import sqrt
    re = True
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            re = False
            break
    if n == 1:
        re = False
    return re