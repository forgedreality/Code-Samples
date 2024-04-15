
const solution = (numbers) => {
    let largest = 0;
    for (let x = 0; x < numbers.length; x++) {
        n = numbers[x];
        largest = Math.max(n, largest);
    }
    return largest;
};

console.log(solution([-2, 0, 10, 1]));

var number = 24;

setTimeout(function() {
    console.log(number);
}, 0);
number = 5;