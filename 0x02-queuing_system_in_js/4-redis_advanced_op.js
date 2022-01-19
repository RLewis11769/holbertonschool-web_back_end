// Use the redis client to store a hash value, then retrieve all as object
const redis = require('redis');
const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });

const updateCache = (key, value) => {
  client.hset('cache', key, value, redis.print);
}

const getCache = () => {
  client.hgetall('cache', (err, obj) => {
    if (err) throw err;
    console.log(obj);
  });
}

updateCache('Portland', '50');
updateCache('Seattle', '80');
updateCache('New York', '20');
updateCache('Bogota', '20');
updateCache('Cali', '40');
updateCache('Paris', '2');
getCache();
