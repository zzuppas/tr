import sqlite3

conn = None

def initialize():
    global conn;
    conn = sqlite3.connect("tr.db")
    cur = conn.cursor()
    result = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clothes';")
    if result.fetchone() is None:
        # Storage classes
        # NULL INTEGER REAL TEXT BLOB
        # https://sqlite.org/datatype3.html
        #result = cur.execute("CREATE TABLE clothes (id INTEGER PRIMARY KEY)")
        cur.execute("CREATE TABLE clothes (id INTEGER PRIMARY KEY, type TEXT, name TEXT, value TEXT)")
        cur.execute("INSERT INTO clothes(type, name, value) VALUES('hat', 'top hat', 'big red top hat')")
        cur.execute("INSERT INTO clothes(type, name, value) VALUES('hat', 'fedora', 'small blue fedora')")
    else:
        result = cur.execute("SELECT * FROM clothes;")
        for x in result:
            print("Clothing is " + str(x))


def close():
    if conn is not None:
        print("closing")
        conn.commit()
        conn.close()
