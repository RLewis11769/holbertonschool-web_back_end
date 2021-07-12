// Change var variables so not overwritten, pay attention to hoisting

export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;

    if (trueOrFalse) {
        const task = true;
        const task2 = false;
    }

    return [task, task2];
}
