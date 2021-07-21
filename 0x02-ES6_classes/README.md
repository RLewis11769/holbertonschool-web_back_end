# JavaScript Classes as of ES6

## Mandatory

***Run with: npm run dev main.js**

### 0-classroom.js
- Implements basic class
    - Used with:
        - 0main.js

### 1-make_classrooms.js
- Creates instances of imported class
    - Adds onto:
        - 0-classroom.js
    - Used with:
        - 1main.js

### 2-hbtn_course.js
- Implements class with getter and setter
    - Used with:
        - 2main.js

### 3-currency.js
- Implements class with method using this.attributes
    - Used with:
        - 3main.js

### 4-pricing.js
- Implements class that uses imported class
    - Use method from imported class
    - Adds onto:
        - 3-currency.js
    - Used with:
        - 4main.js

### 5-building.js
- Implements abstract class with check for classes extending from it
    - Used with:
        - 5main.js

### 6-sky_high.js
- Implements class that inherits from imported class
    - Uses super() to instantiate attribute in parent class (getter/setter in parent)
    - Adds onto:
        - 5-building.js
    - Used with:
        - 6main.js

### 7-airport.js
- Overrides default string description of class
    - Uses Symbol.toStringTag to update type of object from [object Object]
    - Used with:
        - 7main.js

### 8-hbtn_class.js
- Overrides behavior when class cast as primitive type
    - Uses Symbol.toPrimitive to return new behavior
    - Used with:
        - 8main.js

### 9-hoisting.js
- Fix code that incorrectly hoists
    - Declare list as const and then return as opposed to returning const list
    - Used with:
        - 9main.js

### 10-car.js
- Implements class with method that returns new object of class
    - Uses Symbol.species so can return object of parent class or any child classes
    - Used with:
        - 10main.js

## Learning Objectives
- How to define a Class
- How to add methods to a class
- Why and how to add a static method to a class
- How to extend a class from another
- Metaprogramming and symbols
