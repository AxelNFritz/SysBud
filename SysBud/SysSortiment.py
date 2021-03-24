import sqlite3
import pandas as pd

exel = 'Sortiment6.xlsx'
db = 'sysdb6.db'

def get_connection(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    return connection, cursor

def create_db(db_file):
    con, cur = get_connection(db_file)
    print("Creating database...")
    generate_db(exel, cur)
    con.close
    print("Done!")

def generate_db(exel_file, cur):
    df = pd.read_excel(exel_file)
    for row in df.iterrows():
        r = row[1].tolist()
        colums = [r[0], r[3], r[4], r[5], r[7], r[8], r[11], r[12], r[13], r[17], r[18], r[22]] #[0:3:4:5:7:8:11:12:13:17:18:22]
        add_bev(colums, cur)

def add_bev(row, cur):
    statement=f"INSERT INTO dryck_utbud values('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}', '{row[9]}', '{row[10]}', '{row[11]}');"
    cur.execute("begin transaction;")
    try:
        cur.execute(statement)
        cur.execute("commit;")
    except:
        cur.execute("rollback;")
        print(row), print(" Was rejected")

#create_db(db)
