const twoSum = (target, nums) => {
    let out = [];
    for (let i = 0; i < nums.length; i++) {
        let comp = target - nums[i];
        if (comp in nums) {
            out.push(comp, nums[i])
            return out;
        }
    }
    return "Not found";
};

console.log(twoSum(23, [4, 17, 6, 12, 5, 9, 2, 1, 48, 19, 27, 8, 7, 10, 15]));