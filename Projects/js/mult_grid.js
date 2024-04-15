const multiGrid = (grid_a, grid_b) => {
    let sums = 0;

    for (let a_y = 0; a_y < grid_b.length; a_y++) {
        for (let a_x = 0; a_x < a_y.length; a_x++) {
            for (let b_y = 0; b_y < grid_b.length; b_y++) {
                
            }
        }
    }

    for (let i = 0; i < grid[0].length; i++) {
        for (let j = 0; j < grid.length; j++) {
            console.log(grid[j][i]);
        }
    }
    return sums;
};

let a = [
    [ 1,  2,  3,  4,  5 ],
    [ 6,  7,  8,  9,  10 ],
    [ 11, 12, 13, 14, 15 ],
    [ 16, 17, 18, 19, 20 ]
];

let b = [
    [ 21, 22, 23, 24, 25 ],
    [ 26, 27, 28, 29, 30 ],
    [ 31, 32, 33, 34, 35 ],
    [ 36, 37, 38, 39, 40 ]
];

console.log(multiGrid(a, b));