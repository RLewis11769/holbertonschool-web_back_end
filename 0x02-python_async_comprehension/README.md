# Async Comprehension

## Environment Setup

1. Make sure python3 is using version 3.7 or later to use asyncio.run() and other newer functions. Environment setup instructions are found [here](https://github.com/RLewis11769/holbertonschool-web_back_end/tree/main/0x01-python_async_function)

2. Test by:
```
python3 0main.py
python3.7 0main.py
```

3. If python3.7 is working but python3 isn't, copy file with:
```
sudo cp /usr/bin/python3.7 /usr/bin/python3
```

## Tasks

### 0-async_generator.py
- Create async coroutine that loops 10 times, waits 1 second, the yields random number
- Will print complete list of 10 numbers after 10 seconds
	- Used with:
		- 0main.py

### 1-async_comprehension.py
- Create async coroutine that uses async comprehensing to collect numbers from 0-async_generator.py
- Will print complete list of 10 numbers after 10 seconds
	- Used with:
		- 1main.py

### 2-measure_runtime.py
- Create async coroutine that measures time to execute async coroutine in 1-async_comprehension.py 4 times in parallel
- Return amount of time asyncio.gather takes to run 4 async functions
- Since all 4 are running in parallel and each takes 10 seconds, should take ~10 seconds for all 4 to complete
	- Used with:
		- 2main.py

## Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators
