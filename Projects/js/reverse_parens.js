const solution = (inputString) => {
    let start = 0;
    let end = 0;

    while (end < inputString.length) {
        if (inputString[end] === ')') {
            start = end;
            while (inputString[start] !== '(') {
                start--;
            }
            // get the string inside parens
            let content = inputString.slice(start + 1, end);

            // reverse it
            let rev = content.split('').reverse().join('');

            // update inputString
            inputString = inputString.slice(0, start) + rev + inputString.slice(end + 1, inputString.length)

            // we got rid of the '(' and ')', so we are at index end - 1 of new inputString
            end--;
        } else {
            end++;
        }
    }
    return inputString;
};

// reverse string inside of parens
// https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6
let input = 'bar((baz)(blim)foo)';
console.log(solution(input));
