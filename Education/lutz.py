def min1(*args):
    res = args[0]
    for item in args[1:]:
        if item < res:
            res = item
    return res


def min2(first, *args):
    res = first
    for item in args:
        if item < res:
            res = item
    return res


def min3(*args):
    tmp = list(args)
    return sorted(tmp)[0]


def minmax(test, *args):
    res = args[0]
    for arg in args:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y
def maxthan(x, y): return x > y

# print(minmax(maxthan, 1, 2, 3, 4, -2, -5, 3))

# ------------------------------------


# Global and nonlocal vars


def test(a=0):
    count = a

    def do():
        nonlocal count
        count += 1
        print(count, end=' ')
    return do


def test_new(a=0):
    def do():
        do.count += 1
        print(do.count, end=' ')
    do.count = a
    return do


f = test_new()
g = test_new(25)

# for i in range(10):
#     f(); g()
#     print()

# -----------------------------

# Recursion

L = [1, 2, [3, [4, 5, 6, [7, 8], 9], 10], 11, 12]
L_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def summator(L):
    total = 0
    for x in L:
        if not isinstance(x, list):
            total += x
        else:
            total += summator(x)
    return total


# print(summator(L), sum(L_test))

# ----------------------------------
# My own map and zip functions


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


def mymap_2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

# L1 = [1, 2, 3]
# L2 = [1, 2, 3, 4, 5]
#
# print(mymap_2(pow, L1, L2))
# print(mymap_2(sum, (L1,)))


def myzip(*seqs):
    res = []
    seqs = [list(S) for S in seqs]
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


def myzip_new(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))


I = myzip_new('abc', '12345')
print(next(I), next(I), next(I))







