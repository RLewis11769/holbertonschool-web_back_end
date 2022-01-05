// Create http server using http module
const http = require('http');

const app = http
  .createServer((req, res) => {
    // Endpoint will always return "Hello World"
    res.end('Hello Holberton School!');
    // Listen on port 1245
  })
  .listen(1245);

module.exports = app;
