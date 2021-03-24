import sqlite3
import pandas as pd
import uuid

def get_connection(db_file):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    return connection, cursor

def get_species_with_keyword(cursor, a_keyword):
    statement=f"SELECT common FROM protein AS P, species AS S, protein_keywords AS K WHERE K.keyword = '{a_keyword}' AND P.species_id = S.species_id AND K.accession = P.accession GROUP BY common;"
    cursor.execute(statement)

    return cursor.fetchall()


def get_proteins(cursor):
    statement=f"SELECT common AS Art, Count(*) AS Antal FROM protein AS P, species AS S WHERE S.species_id = P.species_id GROUP BY S.species_id;"
    cursor.execute(statement)

    return cursor.fetchall()

def test_func(word, file):
    con, cur = get_connection(file)
    get_species_with_keyword(cur, word)

def get_user_keyword(cursor):
    kw = input ("Enter a keyword: ")
    usr_sp_kw = get_species_with_keyword(cursor, kw)

    return kw, usr_sp_kw

def get_user_species():
    abb = input("Ange förkortning (Helst 2 bokstäver): ")
    lat = input("Ange latisnkt namn: ")
    com = input("Ange artnamn: ")

    return abb, lat, com

def add_species(con, cur, abb, lat, com):
    u_id = uuid.uuid1().int>>105
    statement=f"INSERT INTO species values({u_id}, '{abb}', '{lat}', '{com}');"
    cur.execute("begin transaction;")
    try:
        cur.execute(statement)
        cur.execute("commit;")
        print(f"Du la till ('{abb}', '{lat}', '{com}') i 'species' med species_id som {u_id}")
        z = input("Ny inmatning? (Y/N)")
        if (z == 'Y'):
            present_5(con, cur)
        else:
            print("Hejdå")
            con.close
            exit()
    except:
        cur.execute("rollback;")
        print("Tyvärr felaktig inmatning")
        x = input("Försök igen? (Y/N)")
        if (x == 'Y'):
            present_5(con, cur)
        else:
            print("Hejdå")
            con.close
            exit()



def main(db_file):
    con, cur = get_connection(db_file)

    print("Uppgift 1:")
    present_1(cur)
    print("Uppgift 2:")
    present_2(cur)
    print("Uppgift 3: protein_i.db behövs")
    present_3(cur)
    print("Uppgift 4: ")
    try_present_4(cur)
    print("Uppgift 5: ")
    present_5(con, cur)

    con.close



def present_1(cur):
    arter = get_proteins(cur)
    df_1 = pd.DataFrame(arter)
    df_1.columns = ["Arter", "Antal"]

    return print(df_1)

def present_2(cur):
    t1 = timeit.Timer(stmt="test_func('Glycoprotein', 'protein.db')", setup="from __main__ import test_func")
    t2 = timeit.Timer(stmt="test_func('DA4001', 'protein.db')", setup="from __main__ import test_func")


    sp_with_kw = get_species_with_keyword(cur, "Glycoprotein")
    sp_1 = pd.DataFrame(sp_with_kw)
    sp_1.columns = ["Exempel svar med 'Glycoprotein', Arter"]

    return print("Tid med 'Glycoprotein' (10000): "), print(t1.timeit(10000)), print("Tid med 'DA4001' (10000): "), print(t2.timeit(10000)), print(sp_1)

def try_present_4(cur):
    try:
        present_4(cur)
    except:
        print("Felaktig inmatning")
        x = input("Försök igen? (Y/N)")
        if (x == 'Y'):
            present_4(cur)
        else:
            pass

def present_4(cur):
    usr_kw, usr_sp_kw = get_user_keyword(cur)
    usr_sp = pd.DataFrame(usr_sp_kw)
    usr_sp.columns = ["Arter med keyword " + usr_kw]

    return print(usr_sp)

def present_3(cur):
    try:
        t3 = timeit.Timer(stmt="test_func('Glycoprotein', 'protein_i.db')", setup="from __main__ import test_func")
        t4 = timeit.Timer(stmt="test_func('DA4001', 'protein_i.db')", setup="from __main__ import test_func")
        print("Tid med index 'Glycoprotein' (10000): "), print(t3.timeit(10000)), print("Tid med index 'DA4001' (10000): "), print(t4.timeit(10000))
    except:
        pass


def present_5(con, cur):
    print("Lägg till en 'species' ")
    a, b, c = get_user_species()
    add_species(con, cur, a, b, c)

   
try:
    f = open("protein_c3.db")
    f.close
except:
    print("Du behöver protein_c3.db")
    exit()

main("protein_c3.db")