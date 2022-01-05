// Create http server using Express module
const express = require('express');
const countStudents = require('./3-read_file_async');

module.exports = app = express();
app
  .get('/', (req, res) => res.send('Hello Holberton School!'))
  .get('/students', async (req, res) => {
    const students = await countStudents(process.argv[2]);
    res.send('This is the list of students: ' + students);
    })
  .listen(1245);
