import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", password="", database="student_db"):
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cur = self.conn.cursor(dictionary=True)

    def execute(self, sql, params=None):
        self.cur.execute(sql, params or ())
        self.conn.commit()

    def fetchone(self, sql, params=None):
        self.cur.execute(sql, params or ())
        return self.cur.fetchone()

    def fetchall(self, sql, params=None):
        self.cur.execute(sql, params or ())
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
