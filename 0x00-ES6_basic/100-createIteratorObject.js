export default function createIteratorObject(report) {
  // Returns iterator to go through every employee in every department in report
  // Object does not have @@iterator method with default iteration behavior

  const empList = [];
  for (const emp of Object.values(report.allEmployees)) {
    // Rest operator condenses each value of key
    // Array of strings becomes 2 strings
    empList.push(...emp);
  }

  // Iterable defined directly inside object using computed property
  return {
    // Zero-argument function that returns object
    [Symbol.iterator]() {
      let count = 0;
      return {
        // Iterator must implement next() method
        // next() must have boolean done and value while false
        next() {
          if (count < empList.length) {
            count += 1;
            // Returns are similar to yield here bc of next()
            return { done: false, value: empList[count -1] };
          }
          return { done: true };
        },
      };
    },
  };

// // Default string iterator example
// // Comment out when not used as example
// const str = 'hi';
// console.log(typeof str[Symbol.iterator]); // "function"

// const iterator = str[Symbol.iterator]();
// console.log(iterator  + ''); // "[object String Iterator]"

// console.log(iterator.next()); // { value: "h", done: false }
// console.log(iterator.next()); // { value: "i", done: false }
// console.log(iterator.next()); // { value: undefined, done: true }
// // Just so function will return without error
// console.log(report)
}
