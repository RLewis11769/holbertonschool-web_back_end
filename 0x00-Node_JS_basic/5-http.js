// Create http server using http module
const http = require('http');
const countStudents = require('./3-read_file_async');

// Endpoint for path "/" will return "Hello World"
// Endpoint for path with any other path will return "Not Found"
const app = http
  .createServer(async (req, res) => {
    if (req.url === '/') {
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
      const path = process.argv[2];
      // Count students is returning a dictionary
      const dict = await countStudents(path);
      res.write('This is the list of our students\n');
      // Key of each dict entry is the field to search
      const fields = Object.keys(dict);
      // Count all students in all fields
      const total = fields.reduce((acc, curr) => acc + dict[curr].numStudents, 0);
      res.write(`Number of students: ${total}\n`);
      // Loop through each field
      for (let x = 0; x < fields.length; x += 1) {
        // Each dict field key has value of dict with numStudents and names as keys
        res.write(`Number of students in ${fields[x]}: ${dict[fields[x]].numStudents}. `);
        res.write(`List: ${dict[fields[x]].names.join(', ')}`);
        // If not printing data for last field, add newline
        if (x < fields.length - 1) {
          res.write('\n');
        }
      }
      // Need to end response manually bc dict
      res.end();
    }
  })
  .listen(1245);

module.exports = app;
