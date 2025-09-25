import mariadb
connection= mariadb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'amberward',
    password = 'Dolly12!',
    database = 'people1',
    autocommit = 'True')
print("Successfully connected to MariaDB!")