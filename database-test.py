import sqlite3
conn = sqlite3.connect("c:/test.db")
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE boughtlist
          (ID INT PRIMARY KEY     NOT NULL,
          DateOfOrder           TEXT    NOT NULL,
          OrderNumber            TEXT   NOT NUll,
          NameOfShop             TEXT   NOT NULL ,
          LinkOfShop             TEXT   NOT NULL 
          );''')
print("Table created successfully")
taad=1
c.execute("INSERT INTO boughtlist VALUES(%d,'test','test','California','test');" %taad)
conn.commit()
conn.close()