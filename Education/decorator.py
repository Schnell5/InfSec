class tracer:
    """
    Doesn't work for methods of other classes
    """
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call {0} to {1}'.format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


def tracer1(func):
    """
    Works for simple functions and for methods of classes
    """
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call {0} to {1}'.format(calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(a, b):
    print(a * b)


@tracer1
def spam1(a, b, c):
    print(a + b + c)


if __name__ == '__main__':
    for i in range(3):
        spam(1, 2, 3)
        eggs(5, 6)

        spam1(1, 2, 3)


    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @tracer1
        def giveRaise(self, percent):
            self.pay *= (1 + percent/100)

        @tracer1
        def lastName(self):
            return self.name.split()[-1]

    print('methods...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(10)
    print(sue.pay)
    print(bob.lastName(), sue.lastName())


