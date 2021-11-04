# Python Async/Await

## Tasks

### 0-basic_async_syntax.py
- Asynchronous coroutine that returns float after random amount of time
	- Used with:
		- 0main.py

### 1-concurrent_coroutines.py
- Asynchronous coroutine that returns list of floats after multiple random amounts of time (created by existing function)
	- Import
		- wait_n from 0-basic_async_syntax.py
	- Used with:
		- 1main.py

### 2-measure_runtime.py
- Return total execution time of existing asynchronous coroutine
	- Import
		- wait_random from 1-concurrent_coroutines.py
	- Used with:
		- 2main.py

### 3-tasks.py
- Return task created by existing asynchronous routine
	- Import
		- wait_n from 0-basic_async_syntax.py
	- Used with:
		- 3main.py

### 4-tasks.py
- Asynchronous coroutine that returns list of floats after multiple random amounts of time (created by existing function)
- Essentially same code as 1-concurrent_coroutines.py but using function from 3-tasks.py to create task
	- Import:
		- task_wait_random from 3-tasks.py
	- Used with:
		- 4main.py

## Environment Setup

1. Make sure python3 is version 3.7 or later to use asyncio.run() and other newer functions

```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip python3.7-dev
sudo apt-get install -y python3.7
```

2. Make sure latest version of python3 is being pointed at

```
python3 --version
which python3
python3.7 --version
which python3.7
mv
```

## Learning Objectives

- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module
