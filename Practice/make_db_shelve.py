import shelve
from person import Person
from person import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager(name='Tom Doe', age=50, pay=50000)

db = shelve.open('class-shelve')
db['tom'] = tom
db['bob'] = bob
db['sue'] = sue
db.close()
