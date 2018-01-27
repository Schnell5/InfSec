"""
1. Run this and see the output
2. Comment __contains__ method to see how it works now
3. Comment __contains__ and __iter__ methods to see the new behavior
"""


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print('get[{}]'.format(item), end=' | ')
        return self.data[item]

    def __iter__(self):
        print('iter => ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next: ', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print('contains: ', end='')
        return item in self.data


if __name__ == '__main__':
    x = Iters([1, 2, 3, 4, 5])
    print(3 in x)

    for i in x:
        print(i, end=' | ')

    print()
    print([i ** 2 for i in x])
    print(list(map(bin, x)))

    I = iter(x)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
