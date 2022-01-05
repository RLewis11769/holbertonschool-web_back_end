function readDatabase(path) {
  // Read the file
  fs.readFile(path, (err, data) => {
    if (err) throw err;
    console.log(data);
  });
}
