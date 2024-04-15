
const solution = (prices, start, end) => {
    if (end <= start) {
        // stocks can't be bought
        return 0;
    }

    let profit = 0;

    for (let i = start; i < end; i++) {
        for (let j = i + 1; j <= end; j++) {
            if (prices[j] > prices[i]) {
                let temp = (prices[j] - prices[i]);
                console.log(prices[i], prices[j]);
                profit = Math.max(profit, temp);
            }
        }
    }
    return profit;
};

let p = [13, 10, 8, 4, 10];
console.log(solution(p, 0, p.length - 1));