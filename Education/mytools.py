import time


# ================================= #
# Functions and methods decorators  #
# ================================= #
def timer(label='', trace=True):
    """
    Decorator for calculating the execution time of the function (doesn't work for methods!)
    :param label: your label at the beginning of the output string (default: '')
    :param trace: set to False to disable output messages (default: True)
    :return: class Timer - actual decorator that remembers the original function
    """
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                print('{3} {0}: {1:.5f}, {2:.5f}'.format(self.func.__name__, elapsed, self.alltime, label))
            return result

    return Timer


def timer1(label='', trace=True):
    """
    Decorator for calculating the execution time of the function (works on methods too)
    :param label: your label at the beginning of the output string (default: '')
    :param trace: set to False to disable output messages (default: True)
    :return: decorator function
    """
    def decorator(func):
        """
        Actual decorator object of decorator function 'timer1'
        :param func: original (decorated) function
        :return: result of the original function execution
        """
        def onCall(*args, **kwargs):
            start = time.clock()
            #print('START: {}'.format(start))
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            #print('ELAPSED: {}'.format(elapsed))
            onCall.alltime += elapsed
            if trace:
                print('{3} {0}: {1:.8f}, {2:.8f}'.format(func.__name__, elapsed, onCall.alltime, label))
            return result
        onCall.alltime = 0
        return onCall
    return decorator


# ================================= #
# Class decorators below            #
# ================================= #
def singleton(aClass):
    """
    Function based decorator that allows to create only one instance of decorated class
    """
    instance = None

    def oncall(*args):
        nonlocal instance
        if not instance:
            instance = aClass(*args)
        return instance
    return oncall


class singleton_1:
    """
    Class based decorator that allows to create only one instance of decorated class
    """
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance


def Tracer(aClass):
    """
    Decorator to trace calls to methods and attributes of instance of decorated class
    """
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)

        def __getattr__(self, item):
            print('Trace:', item)
            self.fetches += 1
            return getattr(self.wrapped, item)

    return Wrapper


if __name__ == '__main__':

    @timer1(label='[timer1]==>')
    def listcomp(n):
        return [x * 2 for x in range(n)]


    @timer(label='[timer]==>')
    def mapcall(n):
        return list(map((lambda x: x * 2), range(n)))

    result = listcomp(5)
    listcomp(50000)
    listcomp(500000)
    listcomp(1000000)
    print(result)
    print('All time: {0:.5f}'.format(listcomp.alltime))
    print('')
    result = mapcall(5)
    mapcall(50000)
    mapcall(500000)
    mapcall(1000000)
    print(list(result))
    print(('All time: {0:.5f}'.format(mapcall.alltime)))
    print('map/listcomp = {0}'.format(round(mapcall.alltime / listcomp.alltime, 5)))
    print('\nClass decoration: SINGLETON')

    @singleton
    class Spam:
        def __init__(self, value):
            self.value = value

    @singleton_1
    class Spam_1:
        def __init__(self, value):
            self.value = value

    one = Spam(5)
    two = Spam(77)
    one_1 = Spam_1('abc')
    two_1 = Spam_1('ABC')

    print('one: {0}\ntwo: {1}\none_1: {2}\ntwo_1: {3}'.format(one, two, one_1, two_1))
    print('\nClass decoration: TRACER')

    @Tracer
    class Person:
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate

        @timer1(label='>>>>')
        def pay(self):
            return self.hours * self.rate

        @timer1(label='>>>>')
        def listcomp(self, n):
            return [x * 2 for x in range(n)]

    bob = Person('Bob Jones', 40, 50)
    print(bob.name)
    print(bob.pay())
    bob.listcomp(500000)


