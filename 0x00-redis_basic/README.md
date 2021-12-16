# Redis

## Requirements

Install with:
```
sudo apt-get -y install redis-server
pip3 install redis
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

Might need to start with:
```
service redis-server start
```

Start the CLI with:
```
redis-cli
```

## Relevant File

- exercise.py
	- 

## Tasks

### 0
- Create Cache class
- Initialize instance of Redis client and flush instance in __init__ method
- Add store method to generate random key associated with given data, set data at key, and return key
	- Test with:
		- 0-main.py

### 1
- Add Cache.get method to recover desired format (because Redis stores/returns byte strings only) when passed Callable argument
- Add get_str and get_int methods to parameterize/cast get method with correct conversion function
	- Test with:
		- 1-main.py

### 2
- Count number of times Cache class is called with decorator
- Add count_calls decorator to Cache.store method
- Increase key value on method __qualname__
- Use functools @wraps(method) to create decorator/wrapper
	- Test with:
		- 2-main.py

### 3
- Store history of data/keys stored with decorator
- Add call_history decorator to Cache.store method
- Store list of args in :inputs list with rpush
- Store/return list of keys in :outputs list with rpush
	- Test with:
		- 3-main.py

### 4
- Print history of calls for given function in specified format
- Add replay function to print number of times method called and input/output information

## Advanced

### 5
- Add get_page function to return HTML content of given URL
- Add decorator to track how many times given URL was accessed
- Cache information with 10 second expiration time before removing from redis cache
	- Relevant file:
		- web.py

## Learning Objectives

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache
