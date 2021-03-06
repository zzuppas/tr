import sqlite3
import os

ONE_AND_ONLY_DB = 'tr.db'

class Database:
    def __init__(self, **kwargs):
        self.db_filename = kwargs.get('filename')

    @property
    def db_filename(self):
        return self._db_filename

    @db_filename.setter
    def db_filename(self, filename):
        self._db_filename = filename
        exists = os.path.isfile(filename)
        self._db = sqlite3.connect(filename)
        #self._db.isolation_level = "IMMEDIATE"
        self._db.row_factory = sqlite3.Row
        if not exists:
            self.initialize()

    @db_filename.deleter
    def db_filename(self):
        self.close()

    def close(self):
        self._db.close()
        del self._db_filename

    def initialize(self):
        raise NotImplementedError("You can't triple stamp a double stamp")

    def sql_exec(self, msg, *params):
        self._db.execute(msg, params)
        self._db.commit()


class SavedItems(Database):
    def __init__(self, **kwargs):
        Database.__init__(self, **kwargs)

    def initialize(self):
        # Note: Storage classes are
        # NULL INTEGER REAL TEXT BLOB
        # https://sqlite.org/datatype3.html
        cur = self._db.cursor()
        cur.execute("CREATE TABLE hats (id INTEGER PRIMARY KEY, type TEXT, name TEXT, brief TEXT)")
        cur.execute("INSERT INTO hats(type, name, brief) VALUES('top hat', 'ralph', 'big red top hat')")
        cur.execute("INSERT INTO hats(type, name, brief) VALUES('fedora', 'buster', 'small blue fedora')")
        self._db.commit()

    def describe_hats(self):
        cursor = self._db.execute('select * from {} order by id'.format('hats'))
        hats = {}
        for row in cursor:
            hats[row['id']] = 'The {} named {} is a {}.'.format(row['type'], row['name'].title(), row['brief'])
        return hats

def test():
    items = SavedItems(filename=ONE_AND_ONLY_DB)
    print("There are various hats to choose from.")
    hats = items.describe_hats()
    for hat_id, description in sorted(hats.items()):
        print("{}. ".format(hat_id) + description)
    hat_id = 0
    while True:
        try:
            hat_id = int(input('Which one would you like? > '))
        except ValueError:
            print("Make choice by number")
            continue
        if hat_id not in hats:
            print("That is not a valid option")
            continue
        break
    print("Congrats on choosing \"" + hats[hat_id] + "\"")

if __name__ == "__main__":
    test()
