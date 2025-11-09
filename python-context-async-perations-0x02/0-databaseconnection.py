#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    """Custom class-based context manager for database connection"""

    def __enter__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # If an error happened, rollback, otherwise commit
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

# Using the context manager
with DatabaseConnection() as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
