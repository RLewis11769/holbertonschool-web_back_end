# Pagination

## Tasks

### 0-simple_helper_function.py
- Returns tuple containing start and end index corresponding to range of indexes in a list when given page and page_size
	- Used with:
		- 0main.py

### 1-simple_pagination.py
- Return correct data from CSV file when given useable page and page_size parameters
- Format: each row converted into list with data at each index 
	- Used with:
		- 1main.py

### 2-hypermedia_pagination.py
- Return correct data from CSV file when given useable page and page_size parameters
- Format: each row converted into dict with data at list with key data, plus page, data, next_page, prev_page, and total_pages keys
	- Used with:
		- 2main.py

### 3-hypermedia_del_pagination.py
- Return correct data from CSV even after deleting data/rows
- Format: each row converted into dict with data at list with key data, plus index, next_index, and page_size keys
	- Used with:
		- 3main.py

## Learning Objectives
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner
