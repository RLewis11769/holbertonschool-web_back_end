export default function updateUniqueItems(map) {
  // Update map quantity to 100 if currently 1 (or 'Cannot process' if not map)
  if (map instanceof Map) {
    for (const [key, val] of map) {
        if (val === 1) {
          map.set(key, 100)
        }
    }
    return map
  } else {
    throw new Error('Cannot process');
  }
  
}
