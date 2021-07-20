export default class HolbertonClass {
  // Attributes and methods for HolbertonClass class

  constructor(size, location) {
    // Create and initialize objects
    this.size = size;
    this.location = location;
  }

  // eslint-disable-next-line consistent-return
  [Symbol.toPrimitive](obj) {
    // Overrides default when converting object to "primitive type"
    if (obj === 'number') {
      return this.size;
    }
    if (obj === 'string') {
      return this.location;
    }
  }

  get size() {
    // Getter method to declare size as this._size
    return this._size;
  }

  set size(value) {
    // Setter method to typecheck value passed into size as number
    if (typeof value === 'number') {
      this._size = value;
    } else {
      throw new TypeError('Size must be a number');
    }
  }

  get location() {
    // Getter method to declare location as this._location
    return this._location;
  }

  set location(value) {
    // Setter method to typecheck value passed into location as string
    if (typeof value === 'string') {
      this._location = value;
    } else {
      throw new TypeError('Location must be a string');
    }
  }
}
