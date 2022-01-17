# Queuing Systems

Download, extract, and compile the latest stable Redis version:
```
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
sudo make install
```

Start and test Redis:
```
src/redis-server &
src/redis-cli ping
```

## Tasks

### 0 (dump.rdb)
- Install a Redis instance and add key/value pair
	- Test with:
		```
		$ redis-cli
		ping
		set Holberton School
		get Holberton
		```
