from re import S
import sqlite3

def connect():
    try:
        conn=sqlite3.connect("Banka_autoincrement.db")
        return conn
    except sqlite3.Error as e:
        print(e)
        
def disconnect(conn):
    try:
        conn.close()
    except sqlite3.Error as e:
        print(e)
def printCount(conn, idKom):
    sql="select * from Racun r where r.idkom= ?"
    try:
        cursor=conn.cursor()
        cursor.execute(sql, (idKom,))
        for row in cursor.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")
     
    except sqlite3.Error as e:
        print(e)
def zadatak(conn, idKom, idFil):
    listIdRac=[]
    listStanje=[]
    sql1="select idrac, stanje from racun r where r.idkom= ? and r.stanje<0"
    sql2="select count(*) from stavka  s where s.idrac= ? "
    sql3="insert into stavka (RedBroj, Datum, Vreme, Iznos, IdFil, IdRac) values (?, '2024-28-01','14:38', ?, ?, ?)"
    sql4="update racun set stanje=0   where racun.idrac= ? "
    try:
        cursor=conn.cursor()
        cursor.execute(sql1, (idKom,))
        for row in cursor.fetchall():
            listIdRac.append(row[0])
            listStanje.append(row[1])
       
        sum=0
        while(len(listIdRac)>0):
            idrac=listIdRac.pop(0)
            iznos=-listStanje.pop(0)
            sum=sum+(-iznos)
            cursor.execute(sql2, (idrac,))
            for row in cursor.fetchall():
                brstavki1=row
            brstavki=brstavki1[0]
            brstavki=brstavki+1
            cursor.execute(sql3, (brstavki, iznos, idFil, idrac))
            cursor.execute(sql4, (idrac,))
        conn.commit()
        return sum
    except sqlite3.Error as e:
        print(e)

conn=connect()
printCount(conn, 2) 
print(zadatak(conn, 2, 1))
print("Stanje nakon izvrsene funkcije")
printCount(conn, 2)