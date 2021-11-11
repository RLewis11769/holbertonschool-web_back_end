# Caching

## Starter Module

### BaseCaching
- Defines class that all files inherit from
- Defines put, get, and print_cache methods used in main files 		- put and get are overwritten within task files
	- File:
		- base_caching.py

## Tasks

### 0-basic_cache.py
- Implements cache with no size limit, meaning no data replacement or optimization algorithm
	- Used with:
		- 0main.py

### 1-fifo_cache.py
- Implements caching system based on First-In-First-Out algorithm
- Replaces data in order added
	- 1-2-3-4 replaced by 2-3-4-5 regardless of frequency used
	- Used with:
		- 1main.py

### 2-lifo_cache.py
- Implements caching system based on Last-In-First-Out algorithm
- Replaces data in reverse order added
	- 1-2-3-4 replaced by 1-2-3-5 regardless of frequency used
	- Used with:
		- 2main.py

### 3-lru_cache.py
- Implements caching system based on Least-Recently-Used algorithm
- Replaces data accessed least recently first
	- 1-2-3-4 replaced by 2-3-4-5 UNLESS access 1, for example, in which case replaced by 3-4-1-5
	- Used with:
		- 3main.py

### 4-mru_cache.py
- Implements caching system based on Most-Recently-Used algorithm
- Replaces data accessed most recently first
	- 1-2-3-4 replaced by 1-2-3-5 UNLESS access 1, for example, in which case replaced by 2-3-4-5
	- Used with:
		- 4main.py

## Algorithms

### FIFO
- FIRST In, First Out
	- Organizes data where oldest/first/head of queue is replaced first
![FIFO](https://github.com/RLewis11769/holbertonschool-web_back_end/blob/main/0x00-caching/pics/FIFO.png)

### LIFO
- LAST In, First Out
	- Organizes data where newest/last/tail of queue is replaced first
![LIFO](https://github.com/RLewis11769/holbertonschool-web_back_end/blob/main/0x00-caching/pics/LIFO.png)

### LRU
- LEAST Recently Used
	- Organizes data to keep recently-accessed items near the top of cache. Whenever a new item is accessed, the LRU places it at the top of the cache. When the cache limit has been reached, items that have been accessed less recently will be removed starting from the bottom of the cache.
![LRU](https://github.com/RLewis11769/holbertonschool-web_back_end/blob/main/0x00-caching/pics/LRU.png)

### MRU
- MOST Recently Used
	- Organizes data to keep distantly-accessed items. Whenever a new item is accessed, the LRU places it at the top of the cache. When the cache limit has been reached, items that have been accessed most recently will be removed starting from the top of the cache.
![MRU](https://github.com/RLewis11769/holbertonschool-web_back_end/blob/main/0x00-caching/pics/MRU.png)

### LFU
- Least FREQUENTLY Used
	- Organizes data by using a counter to keep track of how often an entry is accessed. The item with the lowest count is removed first.
![LFU](https://github.com/RLewis11769/holbertonschool-web_back_end/blob/main/0x00-caching/pics/LFU.png)

## Learning Objectives

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have
