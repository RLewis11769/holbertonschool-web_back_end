import Building from './5-building';

// Implement child class/class that extends other class with super

export default class SkyHighBuilding extends Building {
  // Methods and attributes of class inheriting from Building

  constructor(sqft, floors) {
    // Create and initialize objects
    // No need to get/set sqft because done in parent class Building
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
