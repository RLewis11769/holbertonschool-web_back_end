export default function getStudentIdsSum(studentList) {
  // Return sum of ids from studentList using reduce
  // Looking at values of object, adding total and studentList.id where total starts at 0
  const sum = Object.values(studentList).reduce((total, { id }) => total + id, 0);
  return sum;
}
