import os
import psycopg2


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(os.environ["DATABASE_URL"], connect_timeout=5)

    def get_random_joke(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT * FROM jokes ORDER BY random() LIMIT 1""")
        joke = cur.fetchone()
        cur.close()

        return joke
