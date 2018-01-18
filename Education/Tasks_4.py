import math
import mytimer

def adder(**kwargs):
    print('adder:', end=' ')
    sum = kwargs[list(kwargs.keys())[0]]
    for key in list(kwargs.keys())[1:]:
        sum += kwargs[key]
    return sum


# print(adder(a=[1,2,3], b=[4, 5, 6]))
# print(adder(a='abc', b='def'))
# print(adder(a=1, b=4.7))
# print(adder(a=3))


def copyDict(x):
    # return dict(list(x.items()))
    return x.copy()


# D = dict(a=1, b=2, c=3)
# D1 = copyDict(D)
# print(D, D1, D is D1)


def addDict(d1, d2):
    if isinstance(d1, list):
        d1.extend(d2)
    else:
        d1.update(d2)
    return d1


# D = dict(a=1, b=2)
# D1 = dict(a=1, b=77, c=5, d=8)
# print(addDict(D, D1))

def gen1(l):
    res = []
    for x in l:
        res.append(math.sqrt(x))
    return res


def gen2(l):
    return list(map(math.sqrt, l))


def gen3(l):
    return [math.sqrt(x) for x in l]


L = [2, 4, 9, 16, 25]

for func in (gen1, gen2, gen3):
    elapsed, ret = mytimer.timer(func, L)
    print('-'*30)
    print('{0:<9}: {1:.5f} => {2}'.format(func.__name__, elapsed, ret))


