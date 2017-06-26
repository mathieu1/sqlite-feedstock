import sqlite3
with sqlite3.Connection(':memory:') as conn:
    co = list(conn.execute('PRAGMA compile_options;'))
print('sqlite3 compile_options:',co)
assert ('ENABLE_RTREE',) in co