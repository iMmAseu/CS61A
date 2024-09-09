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
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        res = 1
        while k:
            res *= n
            n-=1
            k-=1
        return res

def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    i = 1
    total = 0
    while i <= n:
        if i%k == 0:
            print(i)
            total += 1
        i += 1
    return total

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    k = 1
    prev = 0.1
    total = 0
    last = 0
    while y/k >= 1.0:
        k *= 10
        prev *= 10
        total += (y%k-last)/prev
        last = y%k
    return int(total)
        


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    k = 1
    prev = 0.1
    last = 0
    judge = False
    first = 0
    second = 0
    while n/k >= 1.0:
        k *= 10
        prev *= 10
        first = second
        second = (n%k-last)/prev
        if first == 8 and second == 8:
            judge = True
        last = n%k
    if judge > 1:
        return judge
    else:
        return judge

