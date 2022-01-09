// Helper file used by other functions
import countStudents from '../3-read_file_async';

// readDatabase is identical to countStudents
const readDatabase = (path) => countStudents(path);

module.exports = readDatabase;
