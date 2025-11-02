#!/usr/bin/python3
"""Stream user ages and compute average without loading all ages in memory."""

import seed

def stream_user_ages():
    """Generator yields ages one by one. Single loop using fetchone()."""
    conn = seed.connect_to_prodev()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data;")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        # row is tuple (age,) when not using dictionary cursor
        yield int(row[0])
    cursor.close()
    conn.close()

def average_age():
    """Compute average age using generator. Uses ONE loop over the ages generator."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    avg = total / count if count else 0
    print(f"Average age of users: {avg}")
    return avg

if __name__ == "__main__":
    average_age()
