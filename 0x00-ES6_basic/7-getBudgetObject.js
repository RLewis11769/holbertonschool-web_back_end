export default function getBudgetObject(income, gdp, capita) {
  // Use keyname only when keys/variable for values are the same

  const budget = {
    income,
    gdp,
    capita,
  };
  return budget;
}
