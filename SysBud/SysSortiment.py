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
    df = pd.read_excel(exel_file) #Slowing it all down?
    for row in df.iterrows():
        r = row[1].tolist()
        colums = [r[0], r[3], r[4], r[5], r[7], r[8], r[11], r[12], r[13], r[17], r[18], r[22][:-1]] #[0:3:4:5:7:8:11:12:13:17:18:(r[22][:-1])]
        add_bev(colums, cur)

def add_bev(row, cur):
    statement=f"INSERT INTO dryck_utbud values('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}', '{row[9]}', '{row[10]}', '{row[11]}');"
    cur.execute("begin transaction;") #Move tansaction to generate_db when it all works
    try:
        cur.execute(statement)
        cur.execute("commit;")
    except:
        cur.execute("rollback;")
        print(row), print(" Was rejected")



def search(column, sear, land, varugrupp):
    con, cur = get_connection(db)
    land_state=f"AND land='{land}'"
    varugrupp_state=f"AND varugrupp='{varugrupp}'"
    if land == 'Land': land_state = ""
    if varugrupp == 'Varugrupp': varugrupp_state = ""
    statement=f"SELECT * FROM dryck_utbud WHERE {column} LIKE '%{sear}%' {land_state} {varugrupp_state};"
    cur.execute(statement)
    res = cur.fetchall() #[(tupel0), (tupel1), ...]
    con.close()
    #df = pd.DataFrame(res)
    return res

def top_search(n, sort, land, typ):
    con, cur = get_connection(db)
    statement_ = f"SELECT * FROM dryck_utbud WHERE {column}"


    con.close()
    return res

def apk_add(lis):
    res = []
    for row in lis:
        p = row[11]
        pe = float(p[:-1])
        krl = row[5]
        if pe != 0:
            apk = (pe/krl)*100
        else: 
            apk = 0
        lrow = list(row)
        lrow.append(apk)
        res.append(lrow)

    return res

def apk_sort(lis):
    res = apk_add(lis)
    res = sorted(res, key=lambda x: float(x[12]))[::-1]
    return res    

def krl_sort(lis):
    res = apk_add(lis)
    res = sorted(res, key=lambda x: float(x[5][:-1]))  
    return res  

def apk_search(column, sear, land, varugrupp):
    res = apk_sort(search(column, sear, land, varugrupp))
    return res

def reg_search(column, sear, land, varugrupp):
    res = apk_add(search(column, sear, land, varugrupp))
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

    return (varugrupp_list, land_list)




#apk_search('namn1', 'Fuller')
#create_db(db)
#print(get_spinner_ops())