export default function cleanSet(setToCheck, startStr) {
  // Return values from setToCheck without startStr if values start with startStr

  if (startStr === '' || typeof startStr !== 'string') {
    return '';
  }
  const arr = [];
  for (const val of setToCheck) {
    if (typeof val === 'string' && val.startsWith(startStr)) {
      arr.push(val.slice(startStr.length));
    }
  }
  return arr.join('-');
}
