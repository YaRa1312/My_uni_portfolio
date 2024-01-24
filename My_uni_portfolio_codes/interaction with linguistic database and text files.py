print("Плешивцева Ірина, Прикладна лінгвістика, Лабораторна робота №7")


from multiprocessing import connection
import sqlite3


connection = sqlite3.connect('pol_lab07.s3db')
cursor = connection.cursor()


cursor.execute("SELECT sgN FROM tnoun")
print(cursor.fetchone())


cursor.execute("SELECT plV FROM tnoun WHERE plV LIKE 'o%'")
print(cursor.fetchall())


column_count = 17


for j in range(0,column_count):
    cursor.execute(f"INSERT INTO tnoun (gender, sgN) VALUES ('1','przedmiot')")


for j in range(0,column_count):
    cursor.execute(f"UPDATE tnoun SET (gender, sgN) = ('1','przedmiot') WHERE ID = 331")


connection.commit()
connection.close()
