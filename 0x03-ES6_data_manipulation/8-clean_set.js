export default function cleanSet(setToCheck, startStr) {
  // If values in setToCheck start with startStr, return values without startStr
  if (startStr === '' || typeof startStr !== 'string') {
    return '';
  }
  const arr = [];
  for (const val of setToCheck) {
    if (val.startsWith(startStr)) {
      arr.push(val.slice(startStr.length));
    }
  }
  return arr.join('-');
}
