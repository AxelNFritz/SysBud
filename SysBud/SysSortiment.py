import sqlite3
import pandas as pd


exel = 'Sortiment6 copy.xlsx'
db = 'sysdb8.db'

def get_connection(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    return connection, cursor

def create_db(db_file):
    con, cur = get_connection(db_file)
    print("Creating database...")
    cur.execute("begin transaction;")

    generate_db(exel, cur)

    cur.execute("commit;")
    con.close
    print("Done!")

def generate_db(exel_file, cur):
    print("Reading exel...")
    df = pd.read_excel(exel_file, engine='openpyxl')
    print("Done. Starting to build db..")

    for row in df.iterrows():
        r = row[1].tolist()
        alk = float(r[22][:-1])
        if alk != 0:
            apk = (alk/r[8])*100
        else: 
            apk = 0
        colums = [r[0], r[3], r[4], r[5], r[7], r[8], r[11], r[12], r[13], r[17], r[18], r[22][:-1], apk] #[0:3:4:5:7:8:11:12:13:17:18:(r[22][:-1])]
        add_bev(colums, cur)



def add_bev(row, cur):
    statement=f"INSERT INTO dryck_utbud values('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}', '{row[9]}', '{row[10]}', '{row[11]}','{row[12]}');"
    cur.execute(statement)


def search(target, input, option, sort, varugrupp, land): #(search_target, search_input, search_option, search_varugrupp, search_land)
    con, cur = get_connection(db)

    land_s = "" if land == 'Land' else f"AND land='{land}'"  # result = x if a > b else y
    varugrupp_s = "" if varugrupp == 'Varugrupp' else f"AND varugrupp='{varugrupp}'"
    sort_s = "" if sort == 'Sortering' else f"ORDER BY {sort} DESC" # If Pris/liter it should be ASC
    input_s = input if option == 'Sök' else f"LIMIT {input}"

    if option == 'Sök':
        statement=f"SELECT * FROM dryck_utbud WHERE {target} LIKE '%{input_s}%' {land_s} {varugrupp_s} {sort_s} LIMIT 100;"
    else:
        statement=f"SELECT * FROM dryck_utbud WHERE {target} LIKE '%%' {land_s} {varugrupp_s} {sort_s} {input_s};"

    cur.execute(statement)

    res = cur.fetchall() #[(tupel0), (tupel1), ...]
    con.close()
    return res

def get_spinner_ops():
    con, cur = get_connection(db)
    statement1 = f'SELECT varugrupp FROM dryck_utbud GROUP BY varugrupp;'
    statement2 = f'SELECT land FROM dryck_utbud GROUP BY land;'
    cur.execute(statement1)
    rows1 = cur.fetchall()
    cur.execute(statement2)
    rows2 = cur.fetchall()

    varugrupp_list = list()
    for row in rows1:
        varugrupp_list.append(row[0])

    land_list = list()
    for row in rows2:
        land_list.append(row[0])

    con.close()
    return (varugrupp_list, land_list)


#apk_search('namn1', 'Fuller')
#create_db(db)
#print(get_spinner_ops())
