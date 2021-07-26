export default function createInt8TypedArray(length, position, value) {
  // Return new ArrayBuffer of length with value at position

  if (position > length || position < 0) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const arr = new Int8Array(buffer);

  for (let x = 0; x < length; x += 1) {
    if (x === position) {
      arr[x] = value;
    }
  }
  return new DataView(buffer);
}
