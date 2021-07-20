export default class Building {
  // Attributes and methods of Pricing class (inherits from Currency)

  constructor(sqft) {
    // Create and initialize objects
    this.sqft = sqft;

    // Throw error if class that extends from this class doesn't have specific method
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    // Getter method to declare sqft as this._sqft
    return this._sqft;
  }

  set sqft(value) {
    // Setter method to typecheck value passed into sqft as number
    // if (typeof value === 'number') {
    //   this._sqft = value;
    // } else {
    //   throw new TypeError('Sqft must be a number');
    // }
    this._sqft = value;
  }
}
