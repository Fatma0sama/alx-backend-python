#!/usr/bin/python3
"""
lazy pagination: provide pages lazily with a generator
"""

import seed

def paginate_users(page_size, offset):
    """Helper provided by instructions (keeps DB logic local). Returns list of rows."""
    conn = seed.connect_to_prodev()
    if conn is None:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def lazy_pagination(page_size):
    """Generator that yields pages (lists). Uses only one loop."""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
