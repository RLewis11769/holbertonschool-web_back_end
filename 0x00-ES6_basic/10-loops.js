// Use for...of operator to replace loop

export default function appendToEachArrayValue(array, appendString) {
    const arr = []
    for (const idx of array) {
        idx = appendString + idx;
        arr.push(idx)
    }

    return arr;
}
