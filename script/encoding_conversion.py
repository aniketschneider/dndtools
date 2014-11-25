import sqlite3


def is_text_column(c):
    return (c[1].startswith(u'varchar') or c[1].startswith(u'longtext'))

def convert(s):
    if s == None:
        return None
    return unicode(s, 'latin-1')

db = sqlite3.connect('dnd.sqlite')
db.create_function('FIXENCODING', 1, convert)

cursor = db.execute("select name from sqlite_master where type = 'table'")
tables = map(lambda t: t[0], cursor.fetchall())
dnd_tables = filter(lambda t: t.startswith(u'dnd_'), tables)

for table in dnd_tables:
    cursor = db.execute("pragma table_info({})".format(table))
    columns = map(lambda t: (t[1], t[2]), cursor.fetchall())
    text_columns = filter(is_text_column, columns)

    for column in text_columns:
        print column
        fix_sql = "UPDATE {table} SET \"{column}\" = FIXENCODING(CAST(\"{column}\" AS BLOB))".format(table=table, column=column[0])
        print fix_sql
        db.execute(fix_sql)

    db.commit()
