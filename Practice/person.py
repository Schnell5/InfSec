class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.pay = pay
        self.age = age
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1 + percent/100)

    def __str__(self):
        res = '{0} => {1}'.format(self.__class__.__name__, self.name)
        for key in self.__dict__:
            res += '\n{0:>10} >>> {1}'.format(key, self.__dict__[key])
        return res


class Manager(Person):
    def __init__(self, name, age, pay, job='manager'):
        Person.__init__(self, name, age, pay, job)

    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent + bonus)
