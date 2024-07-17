# Redis Web Cache and Tracker

This project implements an expiring web cache and tracker using Redis. The `get_page` function fetches the HTML content of a given URL, caches the result for 10 seconds, and tracks how many times a URL was accessed.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [File Structure](#file-structure)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/alx-backend-storage.git
    cd alx-backend-storage/0x02-redis_basic
    ```

2. Install the required packages:
    ```sh
    pip install redis requests
    ```

3. Ensure that a Redis server is running on your local machine. You can download and run Redis from [here](https://redis.io/download).

## Usage

The main functionality is implemented in the `web.py` file. The `get_page` function fetches the HTML content of a given URL, caches it with an expiration time of 10 seconds, and tracks the access count.

To use the `get_page` function:

1. Run the script:
    ```sh
    python3 web.py
    ```

2. The script will fetch the content of the specified URL, cache it, and print the access count. The second call to `get_page` should return the cached content if within the 10-second expiration period. The access count will also be displayed.

Example:

```python
url = "http://slowwly.robertomurray.co.uk"
print(get_page(url))
print(get_page(url))
print(redis_client.get(f"count:{url}").decode('utf-8'))

File Structure 

alx-backend-storage/
│
└───0x02-redis_basic/
    │
    ├───exercise.py  # Previous exercise file (not reused in this task)
    ├───main.py      # Script to run and test previous exercises
    └───web.py       # Implementation of the expiring web cache and tracker

