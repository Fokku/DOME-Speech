try:
    import pyodbc
    import pandas as pd
except ImportError:
    import sys
    print("Importing packages failed.")
    sys.exit()

class sqlutil:
    cnxn_str = (r"DRIVER={SQL Server};"
                r"SERVER=sqlsoidemo.database.windows.net;"
                r"DATABASE=dbdome;"
                r"UID=sqladmin;"
                r"PWD=sql(p@ssw0rd)"
                )
    global cnxn
    global cursor
    cnxn = pyodbc.connect(cnxn_str)
    cursor = cnxn.cursor()

    @staticmethod
    def getlist(sql):
        cursor.execute(sql).fetchall()
        return pd.read_sql(sql, cnxn)

    @staticmethod
    def execSQL(sql):
        pass

    @staticmethod
    def close():
        del cnxn
