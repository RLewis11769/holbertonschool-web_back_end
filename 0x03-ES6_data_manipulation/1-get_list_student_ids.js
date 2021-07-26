export default function getListStudentIds(arr) {
  // Return array of ids from list of objects (must use map)

  if (arr instanceof Array) {
    return arr.map((student) => student.id);
  }
  return [];
}
