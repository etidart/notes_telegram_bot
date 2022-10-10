import sqlite3
import json
from datetime import datetime

con = sqlite3.connect("data.db")
cur = con.cursor()

def add_note_db(user_id, name, content):
    now = datetime.now()
    date = "{}.{}.{}".format(now.day, now.month, now.year)
    jarray = json.dumps(content)

    cur.execute("INSERT INTO notes VALUES (?, ?, ?, ?)", [int(user_id), str(name), str(jarray), str(date)])
    con.commit()

