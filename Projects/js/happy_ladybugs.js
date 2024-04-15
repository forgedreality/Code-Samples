// Happy Ladybugs
// https://www.hackerrank.com/challenges/happy-ladybugs/problem
/*
const validateIndex = (value, max) => {
    if (0 <= value <= max - 1) return true;
    return false;
};
*/
const happyLadybugs = (b) => {
    const m = {}
    const a = b.split('')
    const f = a.filter(e => e !== '_')
 
    const unique = (a) => {
        const x = [null, ...a, null]
        for (let i = 1; i < x.length - 1; i++)
            if (x[i] !== null && x[i] !== x[i-1] && x[i] !== x[i+1]) return true
        return false
    };

    f.forEach(e => m[e] = (m[e] || 0) + 1)
    if (a.length === f.length) return unique(f) ? 'NO' : 'YES'
    return Object.values(m).filter(e => e === 1).length ? 'NO' : 'YES'
};


var game_boards = [
    'RBY_YBR',
    'X_Y__X',
    '__',
    'B_RRBR'
];

console.log(game_boards.map(happyLadybugs));


const twosum = (nums, target) => {
    let store = 0;
    for (let [i, n] of nums.entries()) {
        let val = target - n;
        let arr = nums.slice(0, i).concat(nums.slice(i+1));

        if (nums.includes(val)) return [n, nums[nums.indexOf(val)]];
    }
    return -1;
};

console.log(twosum([5,3,10,23,15,7,11,12,6], 30))
