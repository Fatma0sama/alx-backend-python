#!/usr/bin/env python3
import sqlite3

class ExecuteQuery:
    """Reusable query context manager"""

    def __init__(self, query, params=None):
        self.query = query
        self.params = params or ()

    def __enter__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

# Using the context manager
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as cursor:
    results = cursor.fetchall()
    print(results)
