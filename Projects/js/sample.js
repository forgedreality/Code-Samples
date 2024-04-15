const fib = (n, memo = {}) => {
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
};

console.log('Fibonacci: ', fib(100));


/*const gridTraveler = (x, y, memo = {}) => {
    const key = x + "," + y;
    if (key in memo) return memo[key];
    if (x === 0 || y === 0) return 0;
    if (x === 1 && y === 1) return 1;

    memo[key] = gridTraveler(x - 1, y, memo) + gridTraveler(x, y - 1, memo);
    return memo[key];
};

console.log(gridTraveler(64,64))*/


/*const canSum = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    for (let num of numbers) {
        const remainder = targetSum - num;
        const remainderResult = canSum(remainder, numbers, memo);
        if (remainderResult !== null) {
            memo[targetSum] = [ ...remainderResult, num ];
            return memo[targetSum];
        }
    }

    memo[targetSum] = null;
    return null;
};

console.log(canSum(666, [39,1,7,400,67,32,6]));
*/

/*const bestSum = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    let shortestCombination = null;

    for (let num of numbers) {
        const remainder = targetSum - num;
        const remainderCombination = bestSum(remainder, numbers, memo);
        if (remainderCombination !== null) {
            const combination = [...remainderCombination, num];
            if (shortestCombination === null || combination.length < shortestCombination.length) {
                shortestCombination = combination;
            }
            //return memo[targetSum];
        }
    }

    memo[targetSum] = [ shortestCombination ];
    return shortestCombination;
};

console.log(bestSum(6, [2,2,2,3,3,6]));*/


/*const canConstruct = (targetString, wordBank, memo = {}) => {
    if (targetString in memo) return memo[targetString];
    if (targetString === "") return true;
    if (targetString in wordBank) return true;

    for (let word of wordBank) {
        if (targetString.indexOf(word) === 0) {
            const modString = targetString.slice(word.length);
            if (canConstruct(modString, wordBank, memo) === true) {
                memo[targetString] = true;
                return true;
            }
        }
    }

    memo[targetString] = false;
    return false;
};

console.log(canConstruct("tree", ["e","t","xzx","ter","r"]));
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeez", ["e","ee","eee","eeee","eeeee"]));*/


/*const countConstruct = (inputString, wordList, memo = {}) => {
    if (inputString in memo) return memo[inputString];
    if (inputString === "") return 1;

    let totalCount = 0;

    for (let word of wordList) {
        if (inputString.indexOf(word) === 0) {
            const numSolutions = countConstruct(inputString.slice(word.length), wordList, memo);
            totalCount += numSolutions;
        }
    }
    memo[inputString] = totalCount;
    return totalCount;
};

console.log(countConstruct("tree", ["e","t","xzx","ter","r"]));
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeez", ["e","ee","eee","eeee","eeeee"]));*/


/*const allConstruct = (target, wordBank, memo = {}) => {
    if (target in wordBank) return Array(target);
    if (target in memo) return memo[target];
    if (target === "") return Array([]);

    const result = new Array();

    for (let word of wordBank) {
        if (target.indexOf(word) === 0) {
            const suffix = target.slice(word.length);
            const suffixWays = allConstruct(suffix, wordBank, memo);
            const targetWays = suffixWays.map(way => [word, ...way])
            result.push(...targetWays);
        }
    }

    memo[target] = result;
    return result;
};

console.log(allConstruct("test", ["zz","fj","mcm","t","se","te","s"]));*/


/*const tabulationGridTraveler = (x, y) => {
    const table = Array(x + 1).fill().map(() => Array(y + 1).fill(0));

    table[1][1] = 1;

    for(let i = 0; i <= x; i++){
        for (let j = 0; j <= y; j++) {
            const current = table[i][j];
            if (i + 1 <= x) table[i + 1][j] += current;
            if (j + 1 <= y) table[i][j + 1] += current;
        }
    }

    for (let tx = 0; tx <= x; tx++) {
        let row = "";
        for (let ty = 0; ty <= y; ty++) {
            if (ty === 0) row += "|";
            row += " " + table[tx][ty] + " ";
            if (ty === y) row += "|";
        }
        console.log(row);
    }

    return table[x][y];
};

console.log(tabulationGridTraveler(6,9));*/

const countConstruct = (target, wordBank) => {
    const table = Array(target.length + 1).fill(0);
    table[0] = 1;

    for (let i = 0; i <= target.length; i++) {
        for (let word of wordBank) {
            if (target.slice(i, i + word.length) === word) {
                table[i+word.length] += table[i];
            }
        }
    }

    return table[target.length];
};

console.log('countConstruct: ', countConstruct("purple", ["pu", "p", "le", "urpl", "r", "purple", "urple"]));


const allConstruct = (target, wordBank) => {
    const table = Array(target.length + 1).fill().map(() => []);
    table[0] = [[]];

    for (let i = 0; i <= target.length; i++) {
        for (let word of wordBank) {
            if (target.slice(i, i + word.length) === word) {
                const newCombinations = table[i].map(subArray => [ ...subArray, word ]);
                table[i + word.length].push(...newCombinations);
            }
        }
    }
    return table[target.length];
};

console.log('allConstruct: ', allConstruct("abcdef", ["ab", "abc", "cd", "eef", "abcd", "ef", "c"]));


/*const twoSum = (nums, target) => {
    var map = [];
    var result = [];

    for (var i = 0; i < nums.length; i++) {
        if (map[nums[i]] != null) {
            index = map[nums[i]];
            result[0] = index;
            result[1] = i;
            break;
        } else {
            map[target - nums[i]] = i;
        }
    }

    return result;
};
*/

const twoSum = (target, nums) => {
    //FIRST STEP: create an empty Object 
    let numObject = {}   

    //SECOND STEP: use a for-loop to iterate through the array
    for (let eachNum in nums) {
        let otherNum = target - nums[eachNum]; // we'll check for otherNum in the object and if it's there, we got it and can push in our result array.
        if (otherNum in numObject) {
            let resultArr = [];
            resultArr.push(otherNum, nums[eachNum]);
            return resultArr;
        }
        // adding key/value has to go after the if-statement to avoid adding the same index twice.
        // We add the value or a new pair on each iteration.
        numObject[nums[eachNum]] = eachNum;
    }
        return "not found";
};

console.log('twoSum: ', twoSum(46, [1,2,3,4,9,4,39,79,5,6,7]));

const testData = {
    someThing: "test",
    otherThing: "test2",
    mega: 99,
    large: 69
}

const thingy = (function() {
    return function thingy({someThing, mega}) {
        return (`{someThing} {mega}`);
    };
})();

console.log(thingy(testData));