// Connect to the Redis server running locally
const redis = require('redis');
const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });
