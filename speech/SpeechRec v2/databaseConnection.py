import pyodbc
import pandas as pd


class sqlutil:
    cnxn_str = (r"DRIVER={SQL Server};"
                r"SERVER=sqlsoidemo.database.windows.net;"
                r"DATABASE=dbdome;"
                r"UID=sqladmin;"
                r"PWD=sql(p@ssw0rd)"
                )
    cnxn = pyodbc.connect(cnxn_str)
    cursor = cnxn.cursor()

    def getlist(self, sql):
        self.cursor.execute(sql)
        row = self.cursor.fetchall()
        return row

    def execSQL(self, sql):
        self.cursor.execute(sql)
        self.cnxn.commit()
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.cnxn.close()
        print("Connection closed")
a = sqlutil()
print(a.getlist("SELECT * FROM Wordlist"))
a.close()

#some code
"""
INSERT 
"""



