import sqlite3

conn = sqlite3.connect('company.db')
print("Connected")
conn.execute("INSERT INTO Company1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(1,'Rodney','Terer',13,10000.00, 'Consultant')");

conn.commit()
print("Successfully inserted values in company1 table")

conn.close()