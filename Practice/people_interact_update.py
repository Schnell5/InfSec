import shelve
from person import Person

fieldnames = ('name', 'age', 'pay', 'job')
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[{0}] = {1}\nnew? => '.format(field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record

