import Building from './5-building';

export default class SkyHighBuilding extends Building {
  // fkdjkld

  constructor(sqft, floors) {
    // Create and initialize objects
    super().sqft = sqft;
    this.floors = floors;
  }

  evacuationWarningMessage() {
    // Returns string with number of floors
    return `Evacuate slowly the ${this.floors} floors`;
  }

  get floors() {
    // Getter method to declare floors as this._floors
    return this._floors;
  }

  set floors(value) {
    // Setter method to typecheck value passed into floors as number
    if (typeof value === 'number') {
      this._floors = value;
    } else {
      throw new TypeError('Floors must be a number');
    }
  }
}
