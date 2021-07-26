export default function divideFunction(numerator, denominator) {
  // Error handling because number divided by 0 is Infinity

  if (denominator === 0) {
    throw Error('cannot divide by 0');
  } else {
    return (numerator / denominator);
  }
}
