# Redis

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
