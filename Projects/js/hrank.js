"use strict";
// Find pairs that add up as close to target as possible
const intArrSorter = (a, b) => a - b;

const arrProcess = (arr, brr, target) => {
    let m = 0;
    let n = brr.length - 1;

    let smallest_diff = Math.abs(arr[0] + brr[0] - target);
    let closest_pair = [arr[0], brr[0]];

    while (m < arr.length && n >= 0) {
        let num1 = arr[m];
        let num2 = brr[n];
        let current_diff = num1 + num2 - target;
        if (Math.abs(current_diff) < smallest_diff) {
            smallest_diff = Math.abs(current_diff);
            closest_pair = [num1, num2];
        }

        if (current_diff == 0) return closest_pair;
        else if (current_diff < 0) m++;
        else n--;
    }

    return closest_pair;
}

const sumTwoNumbers = (numsArray, target) => {
    let result = [];

    const arrASorted = numsArray[0].sort(intArrSorter);
    const arrBSorted = numsArray[1].sort(intArrSorter);

    if (arrASorted.length - arrBSorted.length <= 0) result = arrProcess(arrASorted, arrBSorted, target);
    else result = arrProcess(arrBSorted, arrASorted, target);

    return (result);
};

console.log(sumTwoNumbers([[-1, 3, 8, 2, 9, 5],[4, 7, 1, 2, 10, 5, 20]], 24));

function sockMerchant(n, ar) {
    let result = 0;
    //let sortedArr = ar.sort(intArrSorter);
    const colors = [];

    for (let i = 0; i < ar.length; i++) {
        let currColor = ar[i];
        if (colors.hasOwnProperty(currColor)) {
            result++;
            delete colors[currColor];
        } else {
            colors[currColor] = 0;
        }
    }
    return result;
}

console.log("sockMerchant: " + sockMerchant(10, [10,20,20,10,10,30,50,10,20]));


/*
 // Base Condition
    if (start > end) return false;

    // Find the middle index
    let mid=Math.floor((start + end)/2);

    // Compare mid with given key x
    if (arr[mid]===x) return true;

    // If element at mid is greater than x,
    // search in the left half of mid
    if(arr[mid] > x)
        return recursiveFunction(arr, x, start, mid-1);
    else

        // If element at mid is smaller than x,
        // search in the right half of mid
        return recursiveFunction(arr, x, mid+1, end);
}

// Driver code
let arr = [1, 3, 5, 7, 8, 9];
let x = 5;

if (recursiveFunction(arr, x, 0, arr.length-1))
    document.write("Element found!<br>");
else document.write("Element not found!<br>");

x = 6;

if (recursiveFunction(arr, x, 0, arr.length-1))
    document.write("Element found!<br>");
else document.write("Element not found!<br>");
*/

function isEven(n) {
    return (n%2==0 ? true : false)
}

// Flip book pages
function pageCount(n, p) {
    if (isEven(p)) p++;

    let result = 0;
    let midValue = Math.floor(n/2)
    let frontToBack = (midValue >= p ? true : false);
    let pageNum = 1;
    //const pagesToFlip = Array.from({length:midValue}, (v,i) => i);

    if (frontToBack) {
        for (let page = 0; page <= midValue; page+=2) {
            if (p == page || p -1 == page) return result;
            else {
                result++;
            }
        }
    }
    else {
        let start = (isEven(n) ? n+1 : n);
        for (let page = start; page > midValue; page-=2) {
            if (p == page || p -1 == page) return result;
            else {
                result++;
            }
        }
    }
    result = Math.min((rightPages[0] - p), (p - rightPages[rightPages.length]));
    return result;
}

console.log("pageCount: " + pageCount(10,6));


function countingValleys(steps, path) {
    let seaLevel = 0;
    let currLevel = 0;
    let valleys = 0;

    for (let i = 0; i < steps; i++) {
        if (path.charAt(i) == "U") {
            currLevel++;
        } else {
            currLevel--;
            if (currLevel == -1) valleys++;
        }
    }
    return valleys;
}

console.log("countingValleys: " + countingValleys(10, "UUDDDUUUUD"));

/*
    // Print the sum of both integer variables on a new line.
    process.stdout.write(i + i2 + '\n');

    // Print the sum of the double variables on a new line.
    process.stdout.write((d + d2).toFixed(1) + '\n');

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    process.stdout.write(s + s2 + '\n');
*/

const budgetProcess = (arr, brr, target) => {
    let smallest_difference = Math.abs(arr[0] + brr[0] - target);

    let current_cost = arr[0] + brr[0];
    if (current_cost > target) return -1;

    for (let x = 0; x < arr.length; x++){
        let n1 = arr[x];
        if (n1 > target) continue;
        for (let y = 0; y < brr.length; y++) {
            let n2 = brr[y];
            if (n2 > target) y = brr.length-1;
            current_cost = ((n1 + n2 <= target) && (n1 + n2 > current_cost) ? n1 + n2 : current_cost);

            let current_difference = current_cost - target;

            if (Math.abs(current_difference) < smallest_difference) {
                smallest_difference = Math.abs(current_difference);
                //current_cost = n1 + n2;
            }

            if (current_difference == 0) return current_cost;
            else if (current_difference < 0) continue;
        }
    }


    return (current_cost > target ? -1 : current_cost);
}

const getMoneySpent = (k, d, b) => {
    let result = -1;
    const sortedKeyboards = k.sort(intArrSorter);
    const sortedDrives = d.sort(intArrSorter);
    for (let i in sortedKeyboards) sortedKeyboards[i] = parseInt(sortedKeyboards[i], 10);
    for (let i in sortedDrives) sortedDrives[i] = parseInt(sortedDrives[i], 10);

    if(sortedKeyboards.length - sortedDrives.length <= 0) {  result = budgetProcess(sortedDrives, sortedKeyboards, b); }
    else result = budgetProcess(sortedKeyboards, sortedDrives, b);

    return result;
};

console.log("getMoneySpent: " + getMoneySpent([3,10,9,8], [4,2,6,12,13,25], 29));


function catAndMouse(x, y, z) {
    return ((Math.abs(x - z) < Math.abs(y - z)) ? "Cat A" : (Math.abs(y - z) < Math.abs(x - z)) ? "Cat B" : "Mouse C");
}

console.log("catAndMouse: " + catAndMouse(2, 4, 6));


/*const calcPossibilities = (matchArr,matchAgainst,filterNum) => {
    let output = new Array();
    let prepOutput = new Array();
    for (let x = 0; x < matchArr.length; x++) {
        let matched = 0;
        for (let y = 0; y < matchAgainst.length; y++) {
            if (matchAgainst[y].includes(matchArr[x])) {
                for (let z = 0; z < matchAgainst[y].length; z++) {
                    matched = matched + (matchAgainst[y][z] == matchArr[x] ? 1 : 0);
                    if (matched == 2) {
                        prepOutput.push(matchAgainst[y]);
                        matched = 0;
                    }
                    matchArr.splice(matchArr[x],1);
                }
            }
        }
    }
    for(let o = 0; o < prepOutput.length; o++) {
        let currRow = prepOutput[o];
        for (let p = 0; p < prepOutput[o].length; p++) {
            let currNum = prepOutput[o][p];
            if (p == 2) output.push(currRow);
        }
    }
    return output;
}

const getCross = (matrix, coords, missingNums) => {
    let sumAddresses = [
        [9,5,1],
        [4,5,6],
        [3,5,7],
        [2,5,8],
        [2,7,6],
        [2,9,4],
        [8,3,4],
        [6,1,8]
    ];

    let curX = coords[0];
    let curY = coords[1];
    let numsList = new Array();
    let possibleMatches = new Array();
    let ignoreNum = matrix[curX][curY];
    let row = new Array(3);
    let col = new Array(3);
    for (let x = 0; x < 3; x++) {
        row = matrix[coords[0]];
        if (x == curX) {
            for (let y = 0; y < 3; y++) {
                col[y] = matrix[y][curY];
            }
        }
    }
    // combine the row and col minus the bad num
    let combinedNums = [...row, ...col].filter((item) => item !== ignoreNum);
    // find the corrected row/col
    possibleMatches = calcPossibilities(combinedNums, sumAddresses, ignoreNum);
    let reducedMatches = new Array();

    for (let i = 0; i < possibleMatches.length; i++) {
        let matched = 0;
        let thisItr = possibleMatches[i].sort(intArrSorter);
        for (let j in thisItr) {
            let currN = thisItr[j];
            if (row.includes(currN) || col.includes(currN)) {
                matched++;
                if(matched == 2) {
                    if (possibleMatches[i][0] + possibleMatches[i][1] + possibleMatches[1][2] == 15) {
                        reducedMatches.push(possibleMatches[i]);
                    }
                    matched = 0;
                }
            }
        }
    }
    for (let p = 0; p < reducedMatches.length; p++) {
        if (reducedMatches[p])
        for (let x = 0; x < row.length; x++) {
            for (let y = 0; y < row.length; y++) {
                if (reducedMatches[p] ) {

                }
            }
        }
    }

    return reducedMatches;
}

const formingMagicSquare = (s) => {
    let output = 0;
    let wrongCoords = new Array();

    let availableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    let removed = new Map();
    for (let e in s) {
        for (let x in s[e]) {
            let curVal = s[e][x];
            let findVal = availableNumbers.indexOf(curVal);
            if (findVal > -1) removed.set(`${e},${x}`, (availableNumbers.splice(findVal,1)));
        }
    }
    let counterX = new Array(3).fill().map(() => 0);
    let counterY = new Array(3).fill().map(() => 0);
    let assembledSquare = [Array(3).fill().map(() => [Array(3).fill().map(() => 0)])];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            counterX[i] += s[i][j];
            counterY[j] += s[j][i];
        }
    }
    for (let t in counterX) {
        if (counterX[t] !== 15) {
            for (let u in counterY) {
                if (counterY[u] !== 15) {
                    wrongCoords.push([parseInt(t),parseInt(u)]);
                }
            }
        }
    }
    for (let w in wrongCoords) {
        let curCoords = wrongCoords[w];
        let possibilities = getCross(s, curCoords, availableNumbers);
    }
    return output;

}

console.log("formingMagicSquare: " + formingMagicSquare([[ 4, 9, 2 ], [ 3, 2, 7 ], [ 8, 1, 5 ]]));*/

const repeatedString = (s, n)  => {
    let size = s.length;
    let repeat = Math.floor(n/size);

    let count = 0;
    let leftHalf = n - (size * repeat);
    let additional = 0;

    for(let x = 0; x < size; x++){
        if(s.charAt(x) == 'a'){
            ++count;
        }
    }

    for(let x = 0; x < leftHalf; x++){
        if(s.charAt(x) == 'a'){
            ++additional;
        }
    }

    repeat = (repeat * count) + additional;
    return repeat;
}

console.log("repeatedString: " + repeatedString("aba", 1000000));


const toPercent = (n) => {
    return n/100;
}

const solve = (meal_cost, tip_percent, tax_percent) => {
    let output = new Number();
    let tip = toPercent(tip_percent);
    let tax = toPercent(tax_percent);
    tip = meal_cost*tip;
    tax = meal_cost*tax;

    output = Math.round(meal_cost+tip+tax).toString();

    //process.stdout.write(output);
    return output;
}

console.log("mealPrice: " + solve(42.55, 15, 10));

const add = (x) => {
    return function(y) { return x+y; };
}

const add2 = (x,y) => {
    return x+y;
}

console.log('Add:', add(4)(10));
console.log('Add2:', add2(4, 10));