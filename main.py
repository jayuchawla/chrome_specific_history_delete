import sqlite3
import re

conn = sqlite3.connect('C:/Users/user/AppData/Local/Google/Chrome/User Data/Default/History')
c = conn.cursor()

def fetchndel(inp):
    res = True
    while res:
        res = False
        ids = []
        stat = "select id,url from urls where url like '%"+inp+"%'"
        for rows in c.execute(stat):
            print(rows)
            id = rows[0]
            ids.append((id,))
        c.executemany('delete from urls where id=?',ids)
        conn.commit()

if __name__=='__main__':
    x = str(input("put web site to del hist of"))
    fetchndel(x)
    conn.close()