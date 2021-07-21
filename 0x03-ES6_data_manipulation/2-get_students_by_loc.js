export default function getStudentsByLocation(listStudents, city) {
  // Return array of objects from listStudents with specified city
  return listStudents.filter((student) => student.city === city);
}
