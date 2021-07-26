import Currency from './3-currency';

// Implement method that references another class
// Implement static method

export default class Pricing {
  // Attributes and methods of Pricing class (inherits from Currency)

  constructor(amount, currency) {
    // Create and initialize objects
    this.amount = amount;
    this.currency = currency;
  }

  displayFullPrice() {
    // Returns attributes in format "amount currency_name (currency_code)"
    // Which is "amount displayFullCurrency()"
    return `${this.amount} ${this.currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    // Returns conversion of amount based on conversionRate
    if (typeof conversionRate !== 'number' || typeof amount !== 'number') {
      throw new TypeError('Unable to convert this amount');
    } else {
      return amount * conversionRate;
    }
  }

  get amount() {
    // Getter method to declare amount as this._amount
    return this._amount;
  }

  set amount(value) {
    // Setter method to typecheck value passed into amount as number
    if (typeof value === 'number') {
      this._amount = value;
    } else {
      throw new TypeError('Amount must be a number');
    }
  }

  get currency() {
    // Getter method to declare currency as this._currency
    return this._currency;
  }

  set currency(value) {
    // Setter method to typecheck value passed into currency as currency
    if (value instanceof Currency) {
      this._currency = value;
    } else {
      throw new TypeError('Currency must be a class object');
    }
  }
}
