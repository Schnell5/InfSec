class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattribute__(self, item):                                   # __getattribute__ intercepts calls for all
                                                                        # attributes (defined and undefined)

        superget = object.__getattribute__                              # We have to use __getattribute__ of object
                                                                        # class (superclass) to prevent looping
        if item == 'acct':
            return superget(self, 'acct')[:-3] + '***'
        elif item == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, item)

    def __setattr__(self, key, value):
        if key == 'name':
            value = value.lower().replace(' ', '_')
        elif key == 'age':
            if value < 0 or value > 130:
                raise ValueError('invalid age')
        elif key == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif key == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[key] = value


if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob.acct, bob.name, bob.remain, bob.addr, sep=' / ')
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob.acct, bob.name, bob.remain, bob.addr, sep=' / ')

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue.acct, sue.name, sue.remain, sue.addr, sep=' / ')

    try:
        sue.age = 200
    except Exception:
        print('Bad age for Sue')

    try:
        sue.remain = 5
    except Exception:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except Exception:
        print('Bad acct for Sue')
