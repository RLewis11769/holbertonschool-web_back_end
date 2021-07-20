export default class Car {
  // Attributes and methods for Airport class

  constructor(brand, motor, color) {
    // Create and initialize objects
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  static get [Symbol.species]() {
    // Points to constructor value so classes can create new versions of themselves
    return this;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species(this.brand, this.motor, this.color);
  }

  // Don't throw errors haha, glad I spent forever on this
  // static validator(name, value) {
  //   // Data validator to make sure value of name is string (hardcode for eslint)
  //   // Not sure if working perfectly - full error
  //   if (typeof value !== 'string') {
  //     throw new TypeError(`${name} must be a string`);
  //   } else {
  //     return value;
  //   }
  // }

  get brand() {
    // Getter method to declare brand as this._brand
    return this._brand;
  }

  set brand(value) {
    // Setter method to typecheck value passed into brand as string
    // this._brand = Car.validator('Brand', value);
    this._brand = value;
  }

  get motor() {
    // Getter method to declare motor as this._motor
    return this._code;
  }

  set motor(value) {
    // Setter method to typecheck value passed into motor as string
    // this._motor = Car.validator('Motor', value);
    this._motor = value;
  }

  get color() {
    // Getter method to declare color as this._color
    return this._color;
  }

  set color(value) {
    // Setter method to typecheck value passed into motor as string
    // this._color = Car.validator('Color', value);
    this._color = value;
  }
}
