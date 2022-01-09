// Controller for user interface for /students routes
import readDatabase from '../utils';

class StudentsController {
  // Student controller

  static getAllStudents(req, res) {
    // Return rendering for students/ page
    res.status(200);
    res.write('This is the list of our students\n');
    // Get info from database (same function as ./3)
    readDatabase(process.argv[2])
      .then((dict) => {
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
    // Return rendering for students/:major pages
    res.status(200);
    // Get info from database (same function as ./3)
    readDatabase(process.argv[2])
      .then((dict) => {
        // Find key of dict that matches whatever is after /students/ in url
        // req.params.major or { major } in req.params
        const major = Object.keys(dict).find((key) => key === req.params.major);
        if (major) {
          res.write(`List: ${dict[major].names.join(', ')}`);
        } else {
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
