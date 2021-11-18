# Personal Data

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
