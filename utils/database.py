import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_folder = os.path.join(BASE_DIR,"data")

os.makedirs(data_folder,exist_ok=True)

db_path = os.path.join(data_folder,"database.db")

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

roll_no TEXT,

branch TEXT,

semester INTEGER,

subject TEXT,

attendance INTEGER,

assignment_marks INTEGER,

quiz_marks INTEGER,

internal_marks INTEGER

)
""")

conn.commit()

conn.close()

print("Database Created Successfully")