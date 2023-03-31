import sqlite3
conn = sqlite3.connect('company.db')
print("Connected")

conn.execute("UPDATE Company1 SET SALARY= 9000000.00 WHERE ID = 1");

conn.commit()
print("Successful")
data = conn.execute("SELECT * FROM Company1")
for rows in data:
    print("ID:", rows[0])
    print("FIRSTNAME:", rows[1])
    print("LASTNAME:", rows[2])
    print("AGE:", rows[3])
    print("SALARY:", rows[4])
    print("TASK:", rows[5])

conn.close()