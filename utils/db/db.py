import sqlite3
import json
import os.path
from datetime import datetime

con = sqlite3.connect('data.db')
cur = con.cursor()

def add_note_db(user_id, title, content) -> any:
    now = datetime.now()
    date = "{}.{}.{}".format(now.day, now.month, now.year)
    jarray = json.dumps(content)

    cur.execute("INSERT INTO notes (user_id, title, content, date) VALUES (?, ?, ?, ?)", (int(user_id), str(title), str(jarray), str(date)))
    con.commit()

def get_all_notes(user_id) -> any:
    cur.execute("SELECT rowid, title FROM notes WHERE user_id = ?", (int(user_id), ))
    return cur.fetchall()

def get_note_content(id) -> any:
    cur.execute("SELECT content FROM notes WHERE rowid = ?", (int(id), ))
    data = cur.fetchone()
    return json.loads(data[0])