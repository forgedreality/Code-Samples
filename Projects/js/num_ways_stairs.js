// num ways to climb stairs

const solution = (n) => {
    // fibonacci solution if only one or two steps at once
    let [one, two] = [1, 1];

    for (let i = 0; i < n - 1; i++) {
        let temp = one;
        one = one + two;
        two = temp;
        console.log(one, two);
    }

    return one;

/*    let allowed_steps = [1, 2, 3];

    if (n === 0) {
        return 1;
    }

    let nums = [];
    for (let i = 0; i < n; i++) {
        nums.push(0);
    }

    nums[0] = 1;

    for (let i = 1; i <= n; i++) {
        let total = 0;
        for (let j of allowed_steps) {
            if (i - j >= 0) {
                total += nums[i - j];
            }
        }
        nums[i] = total;

    }

    return nums[n];
*/};

console.log(solution(3));
/*
def num_ways_to_climb_stairs(n, allowed_steps=[1, 2]):
    # if only considering 1 or 2 steps at a time, we don't need to create a whole list,
    # we can just consider two positions at once.
    if allowed_steps == [1, 2]:
        one, two = 1, 1

        for _ in range(n - 1):
            # add our previous two results, and shift window back by setting two to one's previous value
            one, two = one + two, one

        return one

    # while this method also works for 1 or 2 steps, different numbers of steps makes the sliding window technique
    # more difficult, so we store the entire array of results.
    else:
        if n == 0:
            return 1

        nums = [0] * (n+1)
        nums[0] = 1

        for i in range(1, n+1):
            total = 0
            for j in allowed_steps:
                if i - j >= 0:
                    total += nums[i - j]
            nums[i] = total

        return nums[n]
*/