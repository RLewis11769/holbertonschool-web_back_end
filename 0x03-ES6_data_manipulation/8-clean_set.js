export default function cleanSet(setToCheck, startStr) {
  if (startStr === '') {
    return startStr;
  }
  const arr = [];
  for (const i of setToCheck) {
    if (i.startsWith(startStr)) {
      arr.push(i.slice(startStr.length));
    }
  }
  return arr.join('-');
}
