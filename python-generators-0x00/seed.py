#!/usr/bin/python3
"""seed.py
Utilities to connect to MySQL, create ALX_prodev DB, create user_data table and insert CSV rows.
"""

import mysql.connector
from mysql.connector import errorcode, IntegrityError
import csv
import os

# Update these as needed (or use env vars)
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")

DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"

def connect_db():
    """Connect to MySQL server (no specific DB). Return connection or None."""
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            autocommit=True
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL server: {err}")
        return None

def create_database(connection):
    """Create ALX_prodev database if not exists."""
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
    finally:
        cursor.close()

def connect_to_prodev():
    """Connect to ALX_prodev database and return connection."""
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=DB_NAME,
            autocommit=True
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database {DB_NAME}: {err}")
        return None

def create_table(connection):
    """Create user_data table if not exists."""
    cursor = connection.cursor()
    # use VARCHAR(36) for UUID string
    create_stmt = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        user_id VARCHAR(36) NOT NULL,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        PRIMARY KEY (user_id)
    ) ENGINE=InnoDB;
    """
    try:
        cursor.execute(create_stmt)
        print(f"Table {TABLE_NAME} created successfully")
    finally:
        cursor.close()

def insert_data(connection, csv_path):
    """Insert rows from CSV into user_data if not exist. CSV must have headers:
       user_id,name,email,age
    """
    if not os.path.exists(csv_path):
        print(f"CSV file not found: {csv_path}")
        return

    cursor = connection.cursor()
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        inserted = 0
        for row in reader:
            try:
                cursor.execute(
                    f"INSERT INTO {TABLE_NAME} (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                    (row['user_id'], row['name'], row['email'], int(float(row['age'])))
                )
                inserted += 1
            except IntegrityError:
                # row exists, ignore
                pass
        print(f"Inserted {inserted} rows (ignoring duplicates).")
    cursor.close()
