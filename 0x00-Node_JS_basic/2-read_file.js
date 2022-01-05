// Read database file synchronously
// Log number of students in database
// Log number of students in each field as well as their names
const fs = require('fs');

const countStudents = (path) => {
  // Make sure can read file
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }
  // Get content of file synchronously
  const content = fs.readFileSync(path);
  // Convert to string, split by newline
  let lines = content.toString().split('\n');
  // Filter removes any empty lines, slice removes header
  lines = lines.filter((line) => line !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  // Get list of every "field" field in file
  const field = lines.map((line) => line.split(',')[3]);
  // Get unique values of "field" field
  const eachField = [...new Set(field)];

  for (const fieldName of eachField) {
    // Return list of students for each field
    const studentsPerField = lines
      // This only works because field is last element in line
      // Filter into data for each "field" field
      .filter((line) => line.endsWith(fieldName))
      .map((line) => {
        // Split each line by comma into array
        const stdnt = line.split(',');
        // Return student name (first index)
        return stdnt[0];
      });
    console.log(
      `Number of students in ${fieldName}: ${
        studentsPerField.length
      }. List: ${studentsPerField.join(', ')}`,
    );
  }
};

module.exports = countStudents;
