export default function hasValuesFromArray(setToCheck, arrayValues) {
  // Return boolean if setToCheck contains every num in arrayValues

  return arrayValues.every((num) => setToCheck.has(num));
}
