/* eslint-disable */

export default function taskBlock (trueOrFalse) {
  // Modify variables inside  function so not overwritten inside conditional block

  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // eslint disabled because of this - consts above not overwritten which makes these unused
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}
