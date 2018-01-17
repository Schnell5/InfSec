import mytimer
import sys

reps = 10000
replist = range(reps)


def forLoop():
    res = []
    for x in replist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in replist]


def mapCall():
    return list(map(abs, replist))


def genExpr():
    return list(abs(x) for x in replist)


def genFunc():
    def gen():
        for x in replist:
            yield abs(x)
    return list(gen())


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))
