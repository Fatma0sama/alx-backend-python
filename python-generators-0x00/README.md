# Python Generators - ALX Project (python-generators-0x00)

## Requirements

- Python 3.x
- mysql-connector-python
- MySQL server accessible (set env vars MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT if needed)

## Files

- seed.py : DB setup and CSV loader
- 0-stream_users.py : generator that yields rows one by one
- 1-batch_processing.py : batch generator + processing (users with age > 25)
- 2-lazy_paginate.py : lazy page generator
- 4-stream_ages.py : stream ages and compute average

## How to run

1. Set MySQL credentials via environment variables if not default:
   ```bash
   export MYSQL_USER=root
   export MYSQL_PASSWORD="yourpass"
   export MYSQL_HOST=localhost
   export MYSQL_PORT=3306
   ```
