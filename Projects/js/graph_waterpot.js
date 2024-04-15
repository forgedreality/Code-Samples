const bfs = (matrix) => {
    if (!matrix.length) {
        return [];
    }
    console.log('Before:', matrix);
    let after = matrix;
    

    const queue = [[0,0]];

    const visited = new Array(matrix.length).fill('').map(() => new Array(matrix[0].length).fill(false));

    outer: while (queue.length) {
        const currentPos = queue.shift();
        const row = currentPos[0];
        const col = currentPos[1];

        const rowInvalid = 0 > row || row >= matrix.length;
        const colInvalid = 0 > col || col >= matrix[0].length;
        if (rowInvalid || colInvalid || visited[row][col]) {
            continue;
        }

        visited[row][col] = true;

        directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ];

        if (matrix[row][col] == 0) {
            after[row][col] = '*';
            if (row == matrix.length - 1) {
                break outer;
            }
            for (let dir of directions) {
                queue.push([row + dir[0], col + dir[1]]);
            }
        }

    }
    return after;
};


const check_paths = (grid) => {
    let sum = 0;
    for (let r = 0; r < grid.length; r++) {
        sum += flood_fill(grid, r, 0);
    }
    return sum;
};

const flood_fill = (grid, row, col, visited=[]) => {
    ret = 0;
    if (visited.includes(row + ',' + col)) return 0;
    visited.push(row + ',' + col);

    const rowInbounds = 0 <= row && row < grid.length;
    const colInbounds = 0 <= col && col < grid[0].length;
    if (!rowInbounds || !colInbounds) return 0;

    if (grid[row][col] === 1) return 0;

    if (row == grid.length - 1) return 1;

    ret += flood_fill(grid, row, col + 1, visited);
    ret += flood_fill(grid, row + 1, col, visited);
    ret += flood_fill(grid, row, col - 1, visited);
    ret += flood_fill(grid, row - 1, col, visited);

    return ret;
};


const solution = (pot) => {
    console.log(bfs(pot));
};

solution([
        [0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0]
    ]
);



const solution2 = (maze, startRow, startCol, destRow, destCol) => {
    if (
        (maze[startRow][startCol] == 1 || maze[destRow][destCol] == 1) ||
        startRow > maze.length ||
        startCol > maze[0].length ||
        destRow > maze.length ||
        destCol > maze[0].length
    ) return false;

    let after = maze;
    const queue = [[startRow, startCol]];
    visited =  new Array(maze.length).fill('').map(() => new Array(maze[0].length).fill(false));

    outer: while (queue.length) {
        const currentPos = queue.shift();
        const row = currentPos[0];
        const col = currentPos[1];

        const rowInvalid = 0 > row || row >= maze.length;
        const colInvalid = 0 > col || col >= maze[0].length;
        if (rowInvalid || colInvalid || visited[row][col]) {
            continue;
        }

        visited[row][col] = true;

        if (row == destRow && col == destCol) return true;

        directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ];

        if (maze[row][col] == 0) {
            after[row][col] = '*';
            for (let dir of directions) {
                queue.push([row + dir[0], col + dir[1]]);
            }
        }
    }
    console.log(after);
    return false;
};

console.log(solution2(
    [
        [1, 0, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0],
        [1, 0, 0, 0, 0]
    ],
    0, 1,
    3, 4

));
