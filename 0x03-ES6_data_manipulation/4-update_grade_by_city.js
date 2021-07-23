export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // Returns array of students from specified city with new grade added
  // note: newGrades is array of grade objects that contains studentid and grade

  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      let newGrade = 'N/A';
      if (student.id === 1) {
        newGrade = 5
      }
      return { ...student, grade: newGrade }
    });
    
}
