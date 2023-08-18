#!/usr/bin/python3
# A script that lists all 'states' with a name starting with 'N'
if __name__ == "__main__":
    import MySQLdb
    import sys
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=sys.argv[1], password=sys.argv[2],
                               database=sys.argv[3], use_unicode=True)
    c = database.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE BINARY "N%"
               AND name NOT LIKE BINARY "n%"
               ORDER BY states.id ASC;""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
