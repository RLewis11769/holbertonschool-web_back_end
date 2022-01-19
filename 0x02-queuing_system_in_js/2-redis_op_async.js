// Add setNewSchool and displaySchoolValue functions, then call asynchronously

const redis = require('redis');
const { promisify } = require('util');
const client = redis.createClient();

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
  });

const setNewSchool = async (schoolName, value) => {
  await setAsync(schoolName, value);
  redis.print(null, 'OK');
}

const displaySchoolValue = async (schoolName) => {
  const value = await getAsync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
