# 0x03. Unittests and Integration Tests

## Project Overview

This project contains Python unit and integration tests for utility functions and a GithubOrgClient class. The tests cover:

- **Unit testing**: Testing individual functions and methods to ensure they return expected results for various inputs.  
- **Integration testing**: Testing end-to-end functionality while mocking only external requests.  

The project makes use of:

- `unittest` – Python’s built-in testing framework  
- `parameterized` – For running the same test with multiple inputs  
- `unittest.mock` – For mocking external calls and properties  

## Files

- `utils.py` – Contains utility functions to test  
- `client.py` – Contains `GithubOrgClient` class to test  
- `fixtures.py` – Contains sample data used in integration tests  
- `test_utils.py` – Unit tests for `utils.py`  
- `test_client.py` – Unit and integration tests for `client.py`  

## Running Tests

To run all tests:

```bash
python3 -m unittest discover
