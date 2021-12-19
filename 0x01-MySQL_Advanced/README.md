# MySQL Advanced

## MySQL Server

1. Install with:
```
sudo apt install mysql-server
```

2. Start service
```
server msql start
```

3. Make sure using password:
```
$ mysql -uroot p
Enter password: (Default none - Enter)
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
```

4. To enter database rather than echoing:
```
$ mysql -uroot p
Enter password:
mysql> SHOW DATABASES;
mysql> USE holberton;
mysql> DROP TABLE test;
```

5. Remember:
```
echo "DROP TRIGGER trigger_name;" | mysql -uroot -p holberton
echo "DROP PROCEDURE procedure_name;" | mysql -uroot -p holberton
```

## Project Setup

```
echo "CREATE DATABASE holberton;" | mysql -uroot -p
cat testing/metal_bands.sql | mysql -uroot -p holberton
```

## Mandatory Tasks

### 0-uniq_users.sql
- Creates table with unique email attribute
	- Lessons learned:
		- __Context__: Making an attribute unique directly in the table schema will enforce business rules and avoid bugs in your application
	- Test with:
		```
		$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
		ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
		$ cat 0-uniq_users.sql | mysql -uroot -p holberton
		$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
		$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
		ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
		$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
		```

### 1-country_users.sql
- Creates table with enumeration of countries including default first element
	- Test with:
		```
		$ cat 1-country_users.sql | mysql -uroot -p holberton
		$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
		$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
		$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
		```

### 2-fans.sql
- Ranks countries of origin of bands ordered by total number of fans
	- Lessons learned:
		- __Context__: Calculating/computing is always power intensive. It's better to distribute the load
	- Test files:
		- testing/metal_bands.sql
	- Test with:
		```
		$ cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res
		```

### 3-glam_rock.sql
- Lists all bands with "Glam rock" as a style in a list of styles ranked by longevity
	- Lessons learned:
		- Style column is a list of strings separated by commas with odd consistency - use LIKE and %
		- Longevity is calculated starting with "formed" column and ending with "split" - if "split" contains NULL, use 2020 as value
	- Test files:
		- testing/metal_bands.sql
	- Test with:
		```
		$ cat 3-glam_rock.sql | mysql -uroot -p holberton
		```

### 4-store.sql
- Creates trigger that decreases quantity of items after adding new order
	- After adding to number in orders table, subtract from quantity in items table
	- Lessons learned:
		- __Context__: Updating multiple tables for one action from your application can generate issues: network disconnection, crash, etc. To keep your data in good shape, let MySQL do it for you
	- Test files:
		- testing/4init.sql
		- testing/4main.sql
	- Test with:
		```
		$ cat testing/4init.sql | mysql -uroot -p holberton
		$ cat 4-store.sql | mysql -uroot -p holberton
		$ cat testing/4main.sql | mysql -uroot -p holberton
		```

### 5-valid_email.sql
- Creates trigger that resets valid_email attribute when email has been changed
	- Lessons learned:
		- Before update row with new data, check if "email" field would be different and set valid_email to 0 - use DELIMITER/BEGIN & END
		- __Context__: Not related to MySQL, but perfect for user email validation. Distribute the logic to the database itself
	- Test files:
		- testing/5init.sql
		- testing/5main.sql
	- Test with:
		```
		$ cat testing/5init.sql | mysql -uroot -p holberton
		$ cat 5-valid_email.sql | mysql -uroot -p holberton
		$ cat testing/5main.sql | mysql -uroot -p holberton
		```

### 6-bonus.sql
- Creates stored procedure that adds values to corrections table for given user
	- Lessons learned:
		- If project_name is linked to project id, use project_id. If not, add project_name to project table and use id newly associated with project_name
		- Pass variables to procedure with arguments in form of: IN column_name DATATYPE
		- Declare/identify own variables with @ keyword that are not column names
		- __Context__: Writing code in SQL is a cool level up
	- Test files:
		- testing/6init.sql
		- testing/6main.sql
	- Test with:
		```
		$ cat testing/6init.sql | mysql -uroot -p holberton
		$ cat 6-bonus.sql | mysql -uroot -p holberton
		$ cat testing/6main.sql | mysql -uroot -p holberton
		```

### 7-average_score.sql
- Creates stored procedure that computes and stores average score for given user, updates field in users table
	- Note: Corrections table includes field named "user_id" which is the name of the variable passed to procedure
	- Test files:
		- testing/7init.sql
		- testing/7main.sql
	- Test with:
		```
		$ cat testing/7init.sql | mysql -uroot -p holberton
		$ cat 7-average_score.sql | mysql -uroot -p holberton
		$ cat testing/7main.sql | mysql -uroot -p holberton
		```

### 8-index_my_names.sql
- Creates index on the first letter of the "name" column
	- Lessons learned:
		- On a huge file, like the orginal 143,915KB names.sql file, "SELECT COUNT(name) FROM names WHERE name LIKE 'a%'" would take ~2.19 seconds. After indexing, the exact same query takes ~0.82 seconds
		- Queries run row by row but indexing puts in more of a linked list format, reducing maximum number of searches to find target
		- __Context__: Indexing is not the solution for any performance issue, but it’s a really powerful tool when well used
	- Test files:
		- testing/names.sql
	- Test with:
		```
		$ echo "SELECT COUNT(name) FROM names WHERE name LIKE 'a%';" | mysql -uroot -p holberton
		$ cat 8-index_my_names.sql | mysql -uroot -p holberton 
		$ echo "SHOW index FROM names;" | mysql -uroot -p holberton
		$ echo "SELECT COUNT(name) FROM names WHERE name LIKE 'a%';" | mysql -uroot -p holberton
		```

### 9-index_name_score.sql
- Creates index on the first letter of the "name" column and the "score" column
	- Lessons learned:
		- On a huge file, like the orginal 143,915KB names.sql file, "SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80" would take ~2.4 seconds. After indexing, the exact same query takes ~0.48 seconds
		- Note that this multicolumn index is faster than index in previous task
	- Test files:
		- testing/names.sql
	- Test with:
		```
		$ echo "SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;" | mysql -uroot -p holberton
		$ cat 9-index_name_score.sql | mysql -uroot -p holberton
		$ echo "SHOW index FROM names;" | mysql -uroot -p holberton
		$ echo "SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;" | mysql -uroot -p holberton
		```

### 10-div.sql
- Creates function that returns (a / b) OR 0 if b equals 0 (meaning safely divide without returning NULL)
	- Lessons learned:
		- Pass variables to function with arguments in form of: column_name DATATYPE
		- Specify data type of return
	- Test files:
		- testing/10init.sql
	- Test with:
		```
		$ cat testing/10init.sql | mysql -uroot -p holberton
		$ cat 10-div.sql | mysql -uroot -p holberton
		$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
			- This returns 5.0000 instead of 5 and NULL for 7 / 0
		$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
		```

### 11-need_meeting.sql
- Creates view that lists all students with "score" under 80 and no "last_meeting" or more than a month since date of "last_meeting"
	- Lessons learned:
		- Creates actual table need_meeting in database (?) but is more similar to procedure/trigger as repeatable SELECT statement saved in database as "virtual table"
		- View takes limited space compared to table with exact same data and only includes certain columns for data security
	- Test files:
		- testing/11init.sql
		- testing/11main.sql
	- Test with:
		```
		$ cat testing/11init.sql | mysql -uroot -p holberton
		$ cat 11-need_meeting.sql | mysql -uroot -p holberton
		$ cat testing/11main.sql | mysql -uroot -p holberton
		```

## Advanced

### 100-average_weighted_score.sql
- Creates stored procedure that computes and stores average weighted score for given student
	- "score" is in corrections table and "weight" in projects meaning requires joining tables to calculate. Update "average_score" field in users table to value of calculated average score
	- Test files:
		- testing/100init.sql
		- testing/100main.sql
	- Test with:
		```
		$ cat testing/100init.sql | mysql -uroot -p holberton
		$ cat 100-average_weighted_score.sql | mysql -uroot -p holberton
		$ cat testing/100main.sql | mysql -uroot -p holberton
		```

### 101-average_weighted_score.sql
- Creates stored procedure that computes and store average weighted score for all students
	- Lessons learned:
		- Similar logic to previous task but can't create variable to store info so need to switch around SELECT statement that SETs info in update statement
		- Instead of update-set-where, it's update-join-on-set
	- Test files:
		- testing/101init.sql
		- testing/101main.sql
	- Test with:
		```
		$ cat testing/101init.sql | mysql -uroot -p holberton
		$ cat 101-average_weighted_score.sql | mysql -uroot -p holberton
		$ cat testing/101main.sql | mysql -uroot -p holberton
		```

## Learning Objectives

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures in MySQL
- What is and how to implement functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL
