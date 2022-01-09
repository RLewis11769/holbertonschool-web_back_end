# NoSQL (via MongoDB)

## Installation

1. Install MongoDB with:
```
sudo wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
sudo echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```

2. If the last command fails, try:
```
sudo apt-get install -y mongodb
```

This will NOT get the latest version but will get a working version.

3. If a weird compatability error arises, upgrade Node.js with:
```
npm install n -g && n stable
```

4. Make sure MongoDB is started with:
```
sudo service mongodb status
sudo service mongodb start
```

5. Install PyMongo (and make sure it's working) with:
```
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
```

## Testing

Run 0 and 1 with:
```
cat taskname | mongo
```

Run 2-7 and 100 in the my_db database with:
```
cat taskname | mongo my_db
```

Run 8-11 and 101 as usual for Python functions:
```
./main.py
```

Testing directions for 12 and 102 are listed within task description.

If database collection gets too unwieldy to read properly, drop collection with:
```
db.school.drop()
```

## MongoDB Scripting Tasks (Mongo Shell)

### 0-list_databases
- List all databases in MongoDB

### 1-use_or_create_database
- Create (if needed) and use a new database in MongoDB
	- Make sure to run 0 first

### 2-insert
- Insert a document into the school collection
	- Make sure to run 0 and 1 first

### 3-all
- List all documents in the school collection
	- Make sure to run 0, 1 and 2 first
	- If run 2 multiple times, will list all of them

### 4-match
- List all documents with name="Holberton school" in the school collection
	- Make sure to run 0, 1 and 2 first
	- Test by inserting documents with different name (modify 2 to insert "Holberton School", "Holberton" etc.)

### 5-count
- Count total number of documents in the school collection
	- Make sure to run 0, 1 and 2 first

### 6-update
- Update all documents with name="Holberton school" in the school collection to include a new attribute
	- Make sure to run 0, 1 and 2 first
	- Check by running 4-match

### 7-delete
- Delete all documents with name="Holberton school" in the school collection
	- Make sure to run 0, 1 and 2 first
	- Check by running 4-match

## Python Tasks (PyMongo)

### 8-all.py
- Return all documents in a collection
	- Used with:
		- 8main.py

### 9-insert_school.py
- Insert new document into collection based on kwargs
- Return ID of new document
	- Used with:
		- 9main.py

### 10-update_topics.py
- Update all topics of school document based on name
- Set attribute for document with given name
	- Used with:
		- 10main.py

### 11-schools_by_topic.py
- Returns list of school documents with specific topic
- Shows only matching documents
	- Used with:
		- 11main.py

### 12-log_stats.py
- Print stats about Nginx logs stored in MongoDB
	- Testing:
		```
		curl -o dump.zip -s "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip"
		unzip dump.zip
		mongorestore dump
		./12-log_stats.py
		```

## Advanced Tasks

### 100-find
- List all documents starting with name="Holberton" in the school collection
- Use Regex to match pattern
	- Make sure to run 0, 1 and 2 first
	- Test by inserting documents with different name (modify 2 to insert "Holberton School", "Holberton" etc.)

### 101-students.py
- Returns list of students sorted by average score
- Note that student scores are in value of topics key which contains list of dictionaries with scores at topics:score
- Unwind documents, group, average, sort, and then return aggregation
	- Used with:
		- 101main.py

### 102-log_stats.py
- Add onto 12-log_stats.py to print data about top 10 IPs in nginx collection of logs database
	- Testing:
		```
		./102-log_stats.py
		```

## Learning Objectives
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB
