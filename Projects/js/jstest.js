'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

const intArrSorter = (a, b) => a - b;

const calcGreatestCommonDenominator = (n1, n2) => {
    if (n2 == 0) {
        return n1;
    }
    return calcGreatestCommonDenominator(n2, n1 % n2);
}

const calcLowestCommonMultiple = (n1, n2) => {
    if (n1 == 0 || n2 == 0)
        return 0;
    else {
        let gcd = calcGreatestCommonDenominator(n1, n2);
        return Math.abs(n1 * n2) / gcd;
    }
}

function getTotalX(a, b) {
    // Write your code here
    let sortedA = a.sort(intArrSorter);
    let sortedB = b.sort(intArrSorter);
    let multiples = 0;
    let result = 0;

    let lcm = a[0];
    for(let i = 0; i < a.length; i++) {
        lcm = calcLowestCommonMultiple(lcm, a[i]);
    }

    let gcd = b[0];
    for (let i = 0; i < b.length; i++) {
        gcd = calcGreatestCommonDenominator(gcd, b[i]);
    }

    while (multiples <= gcd) {
        multiples += lcm;
        if (gcd % multiples == 0) result++;
    }

    return result;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const m = parseInt(firstMultipleInput[1], 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const brr = readLine().replace(/\s+$/g, '').split(' ').map(brrTemp => parseInt(brrTemp, 10));

    const total = getTotalX(arr, brr);

    ws.write(total + '\n');

    ws.end();
}

console.log(getTotalX([2,4],[16,32,96]));