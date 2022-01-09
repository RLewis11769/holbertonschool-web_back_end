// Controller for user interface for /students routes
import readDatabase from '../utils';

class StudentsController {
  // Student controller for /students pages

  static getAllStudents(req, res) {
    // Return rendering for /students page
    res.status(200);
    // Get info from database (same function as ./3)
    readDatabase(process.argv[2])
      .then((dict) => {
        res.write('This is the list of our students\n');
        // Key of each dict entry is the field to search
        const fields = Object.keys(dict);
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
  }

  static getAllStudentsByMajor(req, res) {
    // Return rendering for /students/:major pages
    res.status(200);
    // Get info from database (same function as ./3)
    readDatabase(process.argv[2])
      .then((dict) => {
        // List of keys in dict ["CS", "SWE"]
        const fields = Object.keys(dict);
        // Matches whatever is after /students/ in url
        const { major } = req.params;
        if (fields.includes(major)) {
          res.write(`List: ${dict[major].names.join(', ')}`);
        } else {
          res.status(500);
          res.write('Major parameter must be CS or SWE');
        }
      })
      .catch((err) => {
        res.send(err.message);
      })
      .finally(() => {
        res.end();
      });
  }
}

module.exports = StudentsController;
