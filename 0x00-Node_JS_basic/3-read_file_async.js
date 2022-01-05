// Read database file asynchronously
// Log number of students in database
// Log number of students in each field as well as their names
const fs = require('fs').promises;

const countStudents = async (path) => {
  // Define content here so is available after catch block
  let content;
  try {
    content = await fs.readFile(path);
  } catch (error) {
    throw Error('Cannot load the database');
  }
  // Convert to string, split by newline
  let lines = content.toString().split('\n');
  // Filter removes any empty lines, slice removes header
  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  // Get list of every "field" field in file
  const field = lines.map((line) => line.split(',')[3]);
  // Get unique values of "field" field
  const eachField = [...new Set(field)];

  const dict = {};
  for (let x = 0; x < eachField.length; x += 1) {
    // Get number of students in each field
    const numStudents = field.filter((field) => field === eachField[x]).length;
    // Get list of students in each field
    const studentsPerField = lines.filter((line) => line.split(',')[3] === eachField[x]);
    // Get list of names in each field
    const names = studentsPerField.map((student) => student.split(',')[0]);
    // Log number of students in each field
    console.log(`Number of students in ${eachField[x]}: ${numStudents}. List: ${names.join(', ')}`);
    // Add to dictionary
    dict[eachField[x]] = {
      numStudents,
      names,
    };
  }
  return dict;
};

module.exports = countStudents;
