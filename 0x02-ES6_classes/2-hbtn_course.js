export default class HolbertonCourse {
  // Attributes and methods for HolbertonCourse class

  constructor(name, length, students) {
    // Create and initialize objects
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    // Getter method to declare name as this._name
    return this._name;
  }

  set name(value) {
    // Setter method to typecheck value passed into name as string
    if (typeof value === 'string') {
      this._name = value;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  get length() {
    // Getter method to declare length as this._length
    return this._length;
  }

  set length(value) {
    // Setter method to typecheck value passed into length as number
    if (typeof value === 'number') {
      this._length = value;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  get students() {
    // Getter method to declare students as this._students
    return this._students;
  }

  set students(value) {
    // Setter method to typecheck value passed into students as array of strings
    // First checks if array then checks if every i in array is string
    if (typeof value === 'object' && value.every((i) => (typeof i === 'string'))) {
      this._students = value;
    } else {
      throw new TypeError('Students must be an array of numbers');
    }
  }
}
