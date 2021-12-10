#to create db
import sqlite3
with sqlite3.connect('cairndb.db') as con:
    cur=con.cursor()
    table="""CREATE TABLE "cairn_table" (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT, -- rowid
                "date" TEXT,
                "publication" TEXT,
                "author" TEXT,
                "headline" TEXT,
                "items" TEXT                
            )
            """
    cur.execute(table)
    print ("created Cairn_table") 
cur.close()
con.close()

