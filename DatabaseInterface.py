import sqlite3
import random
import time


class DBInterface:
    def __init__(self, db_file):
        self.database = db_file
        self.connection = self._connect()
        if self.connection:
            print("Database connected successfully.")
        self._create_table()
        
    def _connect(self):
        try:
            connection = sqlite3.connect(self.database)
            connection.isolation_level = None
            connection.execute("pragma journal_mode=wal")
            return connection
        except Exception as e:
            print("Can not connect to the database", e)
            return None
        
    def _create_table(self):
        self.connection.execute("create table if not exists book(id integer primary key autoincrement, name, price integer, published)")
        print("table initialized")
        
    def _checkpoint(self, sleep_time=0):
        print("Starting checkpoint...")
        self.connection.execute("pragma journal_size_limit=0")
        self.connection.execute("pragma wal_checkpoint(truncate)")
        time.sleep(sleep_time)
        print("Checkpoint completed....")
        
    def read_db(self):
        count = self.connection.execute("select count(*) from book").fetchone()[0]
        return count
    
    def write_db(self):
        rand_int = random.randint(0, 9)
        price = random.randint(1000, 5000)
        published = random.randint(2000, 2022)
        book = (f"book_{rand_int}", price, str(published))
        self.connection.execute("insert into book(name, price, published) values(?, ?, ?)", book)
        
    def read_db_loop(self, row_count):
        print("Reading database...")
        for i in range(row_count):
            count = self.read_db()
            if i % 100000 == 0:
                print(count)
                self._checkpoint(0)
        print("Completed Reading database")
        self.close()
            
    def write_db_loop(self, row_count):
        print("Started writing database")
        for i in range(row_count):
            self.write_db()
            # checkpoint in the middle
            if i % 10000 == 0:
                self._checkpoint(0)
            
        print("Completed writing database")
        self.close()
        
    def close(self):
        self.connection.close()
        print("Database connection has been closed")
        