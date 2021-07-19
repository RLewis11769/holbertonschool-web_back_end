export default class Airport {
  // Attributes and methods for Airport class

  constructor(name, code) {
    // Create and initialize objects
    this.name = name;
    this.code = code;
  }

  get [Symbol.toStringTag]() {
    // Overrides default string description of object used via Object.prototype.toString() method
    return `${this.code}`;
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

  get code() {
    // Getter method to declare code as this._code
    return this._code;
  }

  set code(value) {
    // Setter method to typecheck value passed into name as string
    if (typeof value === 'string') {
      this._code = value;
    } else {
      throw new TypeError('Code must be a string');
    }
  }
}
