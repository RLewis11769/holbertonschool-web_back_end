function readDatabase(path) {
  // Read the file
  fs.readFile(path, (err, data) => {
    if (err) throw err;
    // Parse the file
    var parsed = JSON.parse(data);
    // Return the parsed file
    return parsed;
  });
}

class StudentsController {
  // App controller

  static getAllStudents(req, res) {
    // Return homepage
    res.status(200);
    readDatabase(process.argv[2]).then(
      (data) => {
        res.write(data);
      }
    )
  }

  static getAllStudentsByMajor(req, res) {
    // Return homepage
    return res.status(200).send("Hello Holberton School!");
  }
}
