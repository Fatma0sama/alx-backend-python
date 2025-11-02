#!/usr/bin/python3
"""
stream rows one-by-one from user_data table using generator
"""

import seed

def stream_users():
    """Generator that yields user rows as dict, one by one. Only one loop used."""
    conn = seed.connect_to_prodev()
    if conn is None:
        return
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT user_id, name, email, age FROM user_data;")
    # single loop: fetchone until None
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
    cursor.close()
    conn.close()
