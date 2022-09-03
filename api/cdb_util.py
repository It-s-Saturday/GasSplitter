import os
import psycopg2
from models.secrets import DB_URL
import gas


class Cockroach:
    def __init__(self):
        self.conn = psycopg2.connect(DB_URL)
        self.cur = self.conn.cursor()

    def _create(self):
        # create the table
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS gas (id INT PRIMARY KEY, price DECIMAL);"
        )
        self.conn.commit()

    def query(self):
        # query the database. if the date is more than a day old, update it.
        self.cur.execute("SELECT * FROM gas;")
        if rows[0][0] < datetime.now() - timedelta(days=1):
            price = gas.get_gas_price()
            self.cur.execute(f"UPDATE gas SET price = {price} WHERE id = 1;")
            self.conn.commit()
        rows = self.cur.fetchall()
        return rows[0][1]


if __name__ == "__main__":
    cockroach = Cockroach()
    cockroach._create()
