export default function getStudentIdsSum(studentList) {
  // Return sum of ids from list of objs (must use reduce)

  // Looking at values of object, adding total and studentList.id where total starts at 0
  return Object.values(studentList).reduce((total, { id }) => total + id, 0);
}
