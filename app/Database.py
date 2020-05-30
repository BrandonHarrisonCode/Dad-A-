import os
import psycopg2


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(os.environ.get("DATABASE_URL"))

    def get_random_joke(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT * FROM jokes ORDER BY random() LIMIT 1""")
        joke = cur.fetchone()
        cur.close()

        return joke
