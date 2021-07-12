// Use computed property names to replace budget object

function getCurrentYear () {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear (income, gdp, capita) {
  return {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita
  };
}
