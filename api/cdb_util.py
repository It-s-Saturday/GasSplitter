import os
import psycopg2
from models.secrets import DB_URL
from gas import get_gas
from datetime import datetime, timedelta


class Cockroach:
    def __init__(self):
        self.conn = psycopg2.connect(DB_URL)
        self.cur = self.conn.cursor()

    def _create(self):
        # create the table
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS gas (id INT PRIMARY KEY, time TIMESTAMP, price DECIMAL);"
        )
        self.conn.commit()

    def query(self):
        # query the database. if the date is more than a day old, update it.
        self.cur.execute("SELECT * FROM gas;")
        rows = self.cur.fetchall()
        flag = False
        try:
            if rows[0][1] < datetime.now() - timedelta(days=1):
                price = get_gas()
                self.cur.execute(f"UPDATE gas SET price = {price} WHERE id = 1;")
                self.conn.commit()
                flag = True
        except IndexError:
            price = get_gas()
            self.cur.execute(
                f"INSERT INTO gas VALUES (1, '{datetime.now()}', {price});"
            )
            self.conn.commit()
            flag = True
        if flag:
            self.cur.execute("SELECT * FROM gas;")
            rows = self.cur.fetchall()
        return rows[0][2]


if __name__ == "__main__":
    cockroach = Cockroach()
    # cockroach._create()
    q = cockroach.query()
    print(q)
