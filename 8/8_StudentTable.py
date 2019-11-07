import sqlite3
conn = sqlite3.connect("STUDENT13.db")
def create():
    print("DATABASE OPENED SUCCESSFULLY\n")
    conn.execute("CREATE TABLE STUDENT2(USN TEXT PRIMARY KEY, NAME TEXT NOT NULL,SEM INT NOT NULL,CGPA FLOAT NOT NULL);")
    conn.commit()
def insert():
    conn.execute("INSERT INTO STUDENT2(USN,NAME,SEM,CGPA)VALUES('1BM18CS416','RAMYASHREE B S',5,8.52)")
    conn.execute("INSERT INTO STUDENT2(USN,NAME,SEM,CGPA)VALUES('1BM18CS417','SALINA M S',5,7.74)")
    conn.execute("INSERT INTO STUDENT2(USN,NAME,SEM,CGPA)VALUES('1BM18CS418','SHUBHA S PATIL',5,8.18)")
    conn.execute("INSERT INTO STUDENT2(USN,NAME,SEM,CGPA)VALUES('1BM18CS420','SHWETA S MALI',5,8.64)")
    conn.execute("INSERT INTO STUDENT2(USN,NAME,SEM,CGPA)VALUES('1BM18CS421','TEJASHWINI V',5,8.46)")
    conn.execute("INSERT INTO STUDENT2(USN,NAME,SEM,CGPA)VALUES('1BM18CS423','YAMUNA B S',5,7.64)")
    conn.commit()
def display():
    cursor = conn.execute("SELECT * FROM STUDENT2")
    print("STUDENT TABLE\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    print("\n\n")
    conn.commit()
def retrieve():
    cursor = conn.execute("SELECT * FROM STUDENT2 WHERE USN='1BM18CS421'")
    print("STUDENT WITH USN 1BM18CS421 DETAILS\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    print("\n\n")
    conn.commit()
def update():
    conn.execute("UPDATE STUDENT2 SET CGPA=8.5 WHERE USN='1BM18CS421'")
    cursor = conn.execute("SELECT * FROM STUDENT2 WHERE USN='1BM18CS421'")
    print("STUDENT WITH USN 1BM18CS421 UPDATED DETAILS\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    print("\n\n")
    conn.commit()
def delete():
    conn.execute("DELETE FROM STUDENT2 WHERE USN='1BM118CS416'")
    cursor= conn.execute("SELECT * FROM STUDENT2")
    print("UPDATED STUDENT TABLE\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    conn.commit()
create()
insert()
display()
retrieve()
update()
delete()

/*OUTPUT
DATABASE OPENED SUCCESSFULLY

STUDENT TABLE

USN = 1BM18CS416
NAME = RAMYASHREE B S
SEM = 5
CGPA = 8.52
---------------
USN = 1BM18CS417
NAME = SALINA M S
SEM = 5
CGPA = 7.74
---------------
USN = 1BM18CS418
NAME = SHUBHA S PATIL
SEM = 5
CGPA = 8.18
---------------
USN = 1BM18CS420
NAME = SHWETA S MALI
SEM = 5
CGPA = 8.64
---------------
USN = 1BM18CS421
NAME = TEJASHWINI V
SEM = 5
CGPA = 8.46
---------------
USN = 1BM18CS423
NAME = YAMUNA B S
SEM = 5
CGPA = 7.64
---------------



STUDENT WITH USN 1BM18CS421 DETAILS

USN = 1BM18CS421
NAME = TEJASHWINI V
SEM = 5
CGPA = 8.46
---------------



STUDENT WITH USN 1BM18CS421 UPDATED DETAILS

USN = 1BM18CS421
NAME = TEJASHWINI V
SEM = 5
CGPA = 8.5
---------------



UPDATED STUDENT TABLE

USN = 1BM18CS416
NAME = RAMYASHREE B S
SEM = 5
CGPA = 8.52
---------------
USN = 1BM18CS417
NAME = SALINA M S
SEM = 5
CGPA = 7.74
---------------
USN = 1BM18CS418
NAME = SHUBHA S PATIL
SEM = 5
CGPA = 8.18
---------------
USN = 1BM18CS420
NAME = SHWETA S MALI
SEM = 5
CGPA = 8.64
---------------
USN = 1BM18CS421
NAME = TEJASHWINI V
SEM = 5
CGPA = 8.5
---------------
USN = 1BM18CS423
NAME = YAMUNA B S
SEM = 5
CGPA = 7.64
---------------*/
