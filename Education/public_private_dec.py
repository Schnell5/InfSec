"""
Public and Private decorators.

Public decorator allows to get and set only attributes that were passed to them during decoration.
Example: @public('data', 'size') - set and get operations will work only for 'data' and 'size'
attributes. All other attributes (if any) are private and cannot be gotten and set.

Private decorator works vice versa.
Example: @private('data', 'size') - set and get operations will prohibited for attributes 'data' and
'size'. All other attributes (if any) are public and can be gotten and set.

P.S. Run this file with -O key to prevent decoration:
#>>> python3 -O public_private_dec.py
"""


trace = False


def tracer(*args):
    if trace:
        print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failif):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class OnInstance:
                def __init__(self, *args, **kwargs):
                    self.__wrapped = aClass(*args, **kwargs)

                def __getattr__(self, attr):
                    tracer('get:', attr)
                    if failif(attr):
                        raise TypeError('private attribute fetch ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)

                def __setattr__(self, attr, value):
                    tracer('set:', attr, value)
                    if attr == '_OnInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failif(attr):
                        raise TypeError('private attribute change ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)

        return OnInstance

    return onDecorator


def private(*attributes):
    return accessControl(failif=lambda attr: attr in attributes)


def public(*attributes):
    return accessControl(failif=lambda attr: attr not in attributes)


if __name__ == '__main__':
    trace = True

    @private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('{0} => {1}'.format(self.label, self.data))

x = Doubler('x is', [1, 2, 3])
y = Doubler('y is', [-10, -20, -30])

print(x.label)
x.display(); x.double(); x.display()

print(y.label)
y.display(); y.double()
y.label = 'Spam'
y.display()

print(x.size())

# This part will raise exceptions for @private decorator
'''
print(x.size())
print(x.data)
x.data = [1, 1, 1]
x.size = lambda s: 0
print(y.data)
print(y.size())
'''