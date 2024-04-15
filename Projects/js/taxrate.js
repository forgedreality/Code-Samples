const solution = (transactions, taxRate) => {
  let numCalls = 0;

  const calculateCostAfterTax = (cost, taxRate) => {
    numCalls += 1;
    return cost * taxRate;
  };

  const unique = (value, index, self) => {
    return self.indexOf(value) === index;
  }

  const computeTotal = taxRate => {
    return cost => {
      return calculateCostAfterTax(cost, taxRate);
    };
  };

  let x = transactions.filter(unique);

  x.map(computeTotal(taxRate));
  return numCalls;
};

console.log(solution([10,24,12,8,10,24], 1.2))
