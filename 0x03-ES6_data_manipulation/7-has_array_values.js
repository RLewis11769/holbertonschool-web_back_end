export default function hasValuesFromArray(setToCheck, arrayValues) {
  // Returns boolean if setToCheck contains every num in arrayValues
  return arrayValues.every((num) => setToCheck.has(num));
}
