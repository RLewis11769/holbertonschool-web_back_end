# JavaScript Basics as of ES6

## Mandatory

<span style="font-size:larger;">***Run with: npm run dev main.js**</span>

### 0-constants.js
- Modify given functions to instantiate variables with keywords
    - taskFirst uses const
    - taskNext uses let
    - Used with:
        - 0main.js

### 1-block-scoped.js
- Modify given function so variables aren't overwritten inside conditional block
    - Pay attention to hoisting
    - Used with:
        - 1main.js

### 2-arrow.js
- Modify given function to use arrow syntax instead of add function
    - Will be anonymous function after
    - Used with:
        - 2main.js

### 3-default-parameter.js
- Modify given function to condense to one line (orig uses if statements for defaults)
    - Define default parameter values
    - Used with:
        - 3main.js

### 4-rest-parameter.js
- Return number of arguments passed
    - Use rest operator syntax to count number of args
    - Used with:
        - 4main.js

### 5-spread-operator.js
- Return each index in two arrays and each character of string
    - Use spread operator syntax to concatenate
    - Used with:
        - 5main.js

### 6-string-interpolation.js
- Modify given function to use template literals to return variable values
    - Use string interpolation instead of concatenating strings and variables with +
    - Used with:
        - 6main.js

### 7-getBudgetObject.js
- Modify given function to use keyname instead of key-value pair
    - Variables and values are the same
    - Used with:
        - 7main.js

### 8-getBudgetCurrentYear.js
- Modify given function to use computed property names as keys
    - Return completed budget object instead of declaring empty dict and adding key-value pairs
    - Used with:
        - 8main.js

### 9-getFullBudget.js
- Modify given function to use method properties
    - Shorthand syntax for method definition based on name
    - Used with:
        - 9main.js

### 10-loops.js
- Modify given function to use for...of operator
    - Replace for...in loop with for...of loop which has no index
        - Essentially for idx of array, idx is shorthand for array[i]
    - Used with:
        - 10main.js

### 11-createEmployeesObject.js
- Return object based on parameters passed in
    - Used with:
        - 11main.js

### 12-createReportObject.js
- Return parameter with return value of function
    - Two returns: object and return of function
    - Used with:
        - 12main.js

## Advanced

### 100-createIteratorObject.js
- Return iterator for object values
    - Essentially @@iterator method for object
    - Based on string default iteration behavior as seen in commented-out example
    - Used with:
        - 100main.js

### 101-iterateThroughObject.js
- Use iterator method from 100-createIteratorObject.js
    - Used with:
        - 100main.js
