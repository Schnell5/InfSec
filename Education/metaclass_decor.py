from types import FunctionType
from decorator import tracer1
from mytools import timer1


class MetaTrace(type):
    def __new__(mcs, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if isinstance(attrval, FunctionType):
                classdict[attr] = tracer1(attrval)
        return type.__new__(mcs, classname, supers, classdict)


# By using this we can choose what decorator should be used
def decorateAll(decorator):
    class MetaTrace(type):
        def __new__(mcs, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if isinstance(attrval, FunctionType):
                    classdict[attr] = decorator(attrval)
            return type.__new__(mcs, classname, supers, classdict)
    return MetaTrace


# The same as metaclass MetaTrace above but by using decorators only
def decorateAllFunc(decorator):
    def decoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if isinstance(attrval, FunctionType):
                setattr(aClass, attr, decorator(attrval))
        return aClass
    return decoDecorate


if __name__ == '__main__':
    class Person(metaclass=decorateAll(timer1(label='>>>>'))):
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate

        # @timer1(label='>>>>')
        def pay(self):
            return self.hours * self.rate

        # @timer1(label='>>>>')
        def listcomp(self, n):
            return [x * 2 for x in range(n)]

    @decorateAllFunc(timer1(label='####'))
    class Person1:
        def __init__(self, name, hours, rate):
            self.name = name
            self.hours = hours
            self.rate = rate

        # @timer1(label='>>>>')
        def pay(self):
            return self.hours * self.rate

        # @timer1(label='>>>>')
        def listcomp(self, n):
            return [x * 2 for x in range(n)]

    bob = Person('Bob Jones', 40, 50)
    sue = Person1('Sue Smith', 35, 45)

    print(bob.name)
    print(bob.pay())
    bob.listcomp(500000)

    print(sue.name)
    print(sue.pay())
    sue.listcomp(400000)
