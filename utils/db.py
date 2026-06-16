import sqlite3

def get_connection():
    return sqlite3.connect("palmtrack.db", check_same_thread=False)

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS workers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
phone TEXT,
salary REAL,
photo TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS harvest(
id INTEGER PRIMARY KEY AUTOINCREMENT,
harvest_date TEXT,
block_name TEXT,
tonnes REAL,
slip_file TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS fertilizer(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fert_type TEXT,
quantity REAL,
cost REAL,
block_name TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS transport(
id INTEGER PRIMARY KEY AUTOINCREMENT,
vehicle_no TEXT,
driver_name TEXT,
tonnes REAL,
charges REAL,
status TEXT
)
""")

conn.commit()
