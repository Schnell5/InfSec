import pickle
import shelve

db = {}

bob = dict(name='Bob Smith', pay=30000, age=42, job='dev')
sue = dict(name='Sue Jones', pay=40000, age=35, job='hdw')
tom = dict(name='Tom', pay=0, age=50, job=None)

db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


def savedb(db):
    dbfile = open('people-pickle', 'wb')
    P = pickle.Pickler(dbfile)
    P.dump(db)
    dbfile.close()


def loaddb(file):
    database = pickle.load(file)
    for key in database:
        print(key, '=>', database[key])


savedb(db)
loaddb(open('people-pickle', 'rb'))

database = shelve.open('people-shelve')
database['bob'] = bob
database['sue'] = sue
database['tom'] = tom
database.close()
