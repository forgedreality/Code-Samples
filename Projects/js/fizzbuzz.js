const fizzbuzz = (num) => {
    let outString = "";
    outString += (num % 3 == 0 ? "fizz" : "") + (num % 5 == 0 ? "buzz" : "");
    return outString == "" ? num : outString;
}

console.log(fizzbuzz(15));


const twoSum = (nums, target) => {
    let out = [];
    let q = [...nums];
    for (let i = 0; i < nums.length; i++) {
        let t = q[i];
        q[i] = -Number.MAX_VALUE;
        let n = target - nums[i];

        if (q.includes(n)) {
            // out = [i, q.indexOf(n)];
            out = [nums[i], q[q.indexOf(n)]];
            break
        }
        q[i] = t;
    }
    return out;
};

var arr = [3,2,4]
console.log('TWOSUM',twoSum(arr, 6));


const twoSumIndexes = (nums, target) => {
    let map = [];
    let result = [];

    for (let i = 0; i < nums.length; i++) {
        if (map[nums[i]] !== undefined) {
            let index = map[nums[i]];
            result[0] = index;
            result[1] = i;
            break;
        } else {
            map[target - nums[i]] = i;
        }
    }

    return (result);
};

console.log(twoSumIndexes([2,7,11,15], 9));

console.log(45 % 0.625);