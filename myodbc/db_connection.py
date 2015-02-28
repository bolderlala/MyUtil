__author__ = 'jl9rf'

import pyodbc

"""
https://code.google.com/p/pyodbc/wiki/GettingStarted
"""
class DBConnect():
    def __init__(self,conn_type,conn_string):
        self.conn_type = conn_type
        self.conn_string = conn_string
        self.cursor = self.connect_database()

    def connect_database(self):
        if self.conn_type == "dsn":
            cnxn = pyodbc.connect('DSN='+self.conn_string)
        elif self.conn_type == "db":
            pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
        return cnxn.cursor()

    def execute_sql(self,select_string):
        self.cursor.execute(select_string)
        row = self.cursor.fetchone()
        return row
        # print 'name:', row.catagoryName
        # print 'name:', row[0]          # access by column index

if __name__ == "__main__":
    myconn = DBConnect ("dsn",'laptop')
    for i in myconn.execute_sql("select * from Haoyuan.dbo.catagory"):
        print i
