class Adder:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        return self.add(other)

    def add(self, x):
        print('Not Implemented')


class ListAdder(Adder):
    def __init__(self, data):
        Adder.__init__(self, data)

    def add(self, x):
        return self.data + x


class DictAdder(Adder):
    def __init__(self, data):
        Adder.__init__(self, data)

    def add(self, x):
        res = self.data.copy()
        res.update(x)
        return res


class MyList:
    def __init__(self, data=[]):
        self.data = []
        for x in data: self.data.append(x)

    def __add__(self, other):
        print('Left add')
        return MyList(self.data + other)

    def __radd__(self, other):
        print('Right add')
        return other + self.data

    def __mul__(self, other):
        print('Multiply it')
        return MyList(self.data * other)

    def __iadd__(self, other):
        print('+= adding')
        return MyList(self.data + other)

    def __getitem__(self, item):
        print('Getting item')
        return self.data[item]

    def __iter__(self):
        print('Iterator returned')
        return self

    def __next__(self):
        print('Iteration in progress: Take an element')
        return next(self.data)

    def append(self, item):
        print('Adding...')
        return self.data.append(item)

    def __len__(self):
        print('Calculate the length')
        return len(self.data)


class MyListSub(MyList):
    addcount = 0

    def __add__(self, other):
        MyListSub.addcount += 1
        print('Operation add was executed {} time(s)'.format(MyListSub.addcount))
