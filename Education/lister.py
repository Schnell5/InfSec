"""
Auxiliary class to print information about other classes that inherit this class

Usage: class <ClassName>(ListTree): ...
       print(<ClassName>)

Returns the tree of classes with attributes that <ClassName> class inherits. Begins from <ClassName> instance and goes
up to <object> class.

Output example:
<Instance of Sub, address: 4360671304:
    _ListTree__visited = {}
    data1 = abc
    data2 = lol

....<Class Sub, address 4323294952:
        __doc__ = <>
        __init__ = <>
        __module__ = <>
        meth = <function Sub.meth at 0x1038ff2f0>

........<Class Super, address 4354784024:
            __dict__ = <>
            __doc__ = <>
            __init__ = <>
            __module__ = <>
            __weakref__ = <>
            meth1 = <function Super.meth1 at 0x1038ff1e0>
........>
....>
"""


class ListTree:
    def __str__(self):
        self.__visited = {}
        return '<Instance of {0}, address: {1}:\n{2}{3}'.format(self.__class__.__name__,
                                                                id(self),
                                                                self.__attrnames(self, 0),
                                                                self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}, address {2}: (see above)>\n'.format(dots,
                                                                         aClass.__name__,
                                                                         id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent + 4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(dots,
                                                                        aClass.__name__,
                                                                        id(aClass),
                                                                        self.__attrnames(aClass, indent),
                                                                        ''.join(genabove),
                                                                        dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0} = <>\n'.format(attr)
            else:
                result += spaces + '{0} = {1}\n'.format(attr, getattr(obj, attr))
        return result
