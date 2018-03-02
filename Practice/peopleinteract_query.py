import shelve

fieldnames = ('name', 'age', 'pay', 'job')
maxfield = max(len(field) for field in fieldnames)
db = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key:
        break
    try:
        record = db[key]
    except Exception:
        print('No such key {0}'.format(key))
    else:
        for field in fieldnames:
            print(field.ljust(maxfield), '=>', getattr(record, field))
