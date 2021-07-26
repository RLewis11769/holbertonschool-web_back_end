export default function iterateThroughObject(reportWithIterator) {
  // Use created default iterator function to join values

  const tobeJoined = [];
  // for loop taken from 100main.js
  for (const item of reportWithIterator) {
    tobeJoined.push(item);
  }
  // Join requires array and returns string
  return tobeJoined.join(' | ');
}
