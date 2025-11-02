#!/usr/bin/python3
"""Batch processing: stream users in batches and print users with age > 25."""

import seed

def stream_users_in_batches(batch_size):
    """Yield batches (lists) of dict rows. Uses one loop internally to page."""
    offset = 0
    conn = seed.connect_to_prodev()
    if conn is None:
        return
    cursor = conn.cursor(dictionary=True)
    while True:
        cursor.execute("SELECT user_id, name, email, age FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows
        offset += batch_size
    cursor.close()
    conn.close()

def batch_processing(batch_size):
    """Process batches and print users with age > 25.
       Total loops used: outer loop over batches + inner loop over rows = 2 loops.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user.get('age', 0) > 25:
                print(user)
