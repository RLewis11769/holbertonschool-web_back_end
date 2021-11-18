# Personal Data

## Task Files

- filtered_logger.py
- encrypt_password.py

## Tasks

### filtered_logger.py

#### 0
- Adds filter_datum function
- Uses re.sub to return given string with obfuscated values of passed fields
	- Used with:
		- 0main.py

#### 1
- Adds RedactingFormatter class and filter_datum method
- Returns filtered log records using filter_datum and logging.Formatter to format
	- Used with:
		- 1main.py

#### 2
- Adds get_logger function
- Creates and returns logger with specified settings and PII_FIELDS redacted
	- Used with:
		- 2main.py
		- user_data.csv

#### 3
- Adds get_db function
- Returns connector to database with credentials passed in from environment
	- Used with:
		- 3main.py
		- 3main.sql
	- Test with:

		```
		$ cat 3main.sql | mysql -uroot -p
		$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
		$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./3main.py
		```
	- Expected result:
		````
		2
		````

#### 4
- Add main function so filtered_logger.py can be standalone file
- Obtain database connection, retrieve all rows in users table, and display each row in specified, filtered format
	- Used with:
		- 4main.sql
	- Test with:

		```
		$ cat 4main.sql | mysql -uroot -p
		$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
		$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py
		```
	- Expected result:
		```
		[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;
		[HOLBERTON] user_data INFO 2019-11-19 18:37:59,621: name=***; email=***; phone=***; ssn=***; password=***; ip=f724:c5d1:a14d:c4c5:bae2:9457:3769:1969; last_login=2019-11-14 06:16:19; user_agent=Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I9100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;
		```

### encrypt_password.py

#### 5
- Adds hash_password function
- Returns salted, hashed password as byte string from given unencoded string password
	- Used with:
		- 5main.py

#### 6
- Adds is_valid function
- Returns boolean as validation that provided password matches hashed password
	- Used with:
		- 6main.py

## MySQL Database

1. Make sure MySQL is installed with:

```
$ sudo apt-get install mysql-client
```

2. Make sure you can use the 'mysql-connector-python' module to connect to the MySQL database

```
$ pip3 install mysql-connector-python
```

3. Make sure the MySQL server is started:

```
$ sudo service mysql start
```

4. Change the root user's password to 'root' by changing it with the database itself:

```
$ sudo MySQL
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
quit;
```

5. Add data to the database with:

```
$ cat main.sql | mysql -uroot -p
```

## bcrypt Library

Make sure bcrypt package is installed with one of:

```
pip install bcrypt
pip install py-bcrypt
```

## Learning Objectives

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables
