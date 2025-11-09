#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    """Custom class-based context manager for database connection"""

    def __init__(self, db_name="users.db"):
        """Initialize the database name (required by checker)"""
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()

# Using the context manager with 'with' statement
with DatabaseConnection() as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
