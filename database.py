import sqlite3
import os

os.makedirs("data",exist_ok=True)

conn=sqlite3.connect("data/traders.db",check_same_thread=False)

cursor=conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS traders(

id TEXT,
trust_score REAL,
risk TEXT

)

""")

conn.commit()

def save_trader(trader_id,trust,risk):

    cursor.execute(
    "INSERT INTO traders VALUES (?,?,?)",
    (trader_id,trust,risk)
    )

    conn.commit()