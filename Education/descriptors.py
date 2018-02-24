class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name                                # Call Name.__set__()
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return instance._name

        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance._name = value
    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return instance._age

        def __set__(self, instance, value):
            if value < 0 or value > 130:
                raise ValueError('invalid age')
            else:
                instance._age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return instance._acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number')
            else:
                instance._acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):                 # We have to use __set__ method to prevent assignment of
            raise TypeError('cannot set remain')            # the 'remain' attribute to the instance of
                                                            # the class CardHolder. If we won't use __set__ method here
                                                            # and will perform 'obj.remain = value' somewhere in the
                                                            # __main__ section of the code the instance of the
                                                            # class CardHolder will get it's own 'remain' attribute
                                                            # (at the instance level) and Remain() descriptor won't work
                                                            # for this instance.
    remain = Remain()


if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print(bob.acct, bob.name, bob.remain, bob.addr, sep=' / ')
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print(bob.acct, bob.name, bob.remain, bob.addr, sep=' / ')

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    print(sue.acct, sue.name, sue.remain, sue.addr, sep=' / ')
    print(bob.name, bob.acct, bob.age)
    print(sue.name, sue.acct, sue.age)

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
