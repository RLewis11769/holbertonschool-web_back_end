export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // Returns array of students from specified city with new grade added
  // note: newGrades is array of grade objects that contains studentid and grade

  // Returns list with changes made based on filter/map
  return studentList
    // Filters down to only students where location matches
    .filter((student) => student.location === city)
    // Does everything in function to every student in studentList
    .map((student) => {
      // Default of new_grade is N/A
      let addGrade = 'N/A';
      // Go through newGrades array and find studentId that matches this student
      newGrades.forEach((grade) => {
        if (grade.studentId === student.id) {
          // Change addGrade from N/A to grade in newGrades
          addGrade = grade.grade;
        }
      });
      // console.log(obj);
      console.log(addGrade);
      // Returns everything in each student obj with grade from addGrade added to obj
      return { ...student, grade: addGrade };
    });
}
