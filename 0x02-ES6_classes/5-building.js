export default class Building {
  // Attributes and methods of Pricing class (inherits from Currency)

  constructor(sqft) {
    // Create and initialize objects
    this.sqft = sqft;

    // Throw error if class that extends from this class doesn't have specific method
    // this.constructor===Building refers to any classes extending this "abstract" class
    // Needs to be in constructor
    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    // Getter method to declare sqft as this._sqft
    return this._sqft;
  }

  set sqft(value) {
    // Setter method that just sets value, no typechecking due to main file
    this._sqft = value;
  }
}
