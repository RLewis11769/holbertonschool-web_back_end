// Create http server using Express module
const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app
  .get('/', (req, res) => res.send('Hello Holberton School!'))
  .get('/students', async (req, res) => {
    res.write('This is the list of our students\n');
    await countStudents(process.argv[2])
      .then((dict) => {
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
      })
      .catch((err) => {
        res.write(err.message);
      })
      .finally(() => {
        res.end();
      });
  })
  .listen(1245);

module.exports = app;
