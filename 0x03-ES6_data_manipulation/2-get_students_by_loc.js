export default function getStudentsByLocation(listStudents, city) {
  // Return array of objects with specified city (must use filter)

  return listStudents.filter((student) => student.location === city);
}
