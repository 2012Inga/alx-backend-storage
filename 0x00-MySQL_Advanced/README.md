# 0x00-MySQL_Advanced

## Task 0: We are all unique!

This project contains a SQL script `0-uniq_users.sql` that creates a table named `users` with the following attributes:
- `id`: an integer, never null, auto-incremented, and the primary key.
- `email`: a string (255 characters), never null, and unique.
- `name`: a string (255 characters).

### Usage

To execute the script and create the `users` table, run the following command:

```bash
$ cat 0-uniq_users.sql | mysql -uroot -p your_database_name`
