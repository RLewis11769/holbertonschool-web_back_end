export default function createReportObject(employeesList) {
  // Return object and use return of function

  return {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      // Return number of keys in allEmployees object
      return Object.keys(this.allEmployees).length;
    },
  };
}
