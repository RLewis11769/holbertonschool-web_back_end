// Implement method in class

export default class Currency {
  // Attributes and methods for Currency class

  constructor(code, name) {
    // Create and initialize objects
    this.code = code;
    this.name = name;
  }

  displayFullCurrency() {
    // Returns attributes in format "name (code)"
    return `${this.name} (${this.code})`;
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
}
