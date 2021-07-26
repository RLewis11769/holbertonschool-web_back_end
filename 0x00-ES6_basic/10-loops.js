export default function appendToEachArrayValue(array, appendString) {
  // Use for...of loop (remember: no array[idx])

  const arr = [];
  for (const idx of array) {
    const val = appendString + idx;
    arr.push(val);
  }

  return arr;
}
