export default function iterateThroughObject(reportWithIterator) {
  const tobeJoined = [];
  // for loop taken from 100main.js
  for (const item of reportWithIterator) {
    tobeJoined.push(item);
  }
  // Join requires array
  return tobeJoined.join(' | ');
}
