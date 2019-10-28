# wdmain.py = window -> main
# 2019.10.03.
# V0.01
# by Svab

import sqlite3


conn = sqlite3.connect('dnd.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM monsters ORDER BY rowid'):
    print(row)