// Create http server using Express module
const express = require('express');

const app = express();
app
  .get('/', (req, res) => res.send('Hello Holberton School!'))
  .listen(1245);

module.exports = app;
