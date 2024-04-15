const checkCoords = (matrix, node) => {
    if (node[0] < 0 || node[1] < 0 || node[1] >= matrix[0].length || node[0] >= matrix.length || matrix[node[0]][node[1]] == 1) {
        return false;
    }
    return true;
};

const getCoordStr = (coords) => {
    return coords[0] + ',' + coords[1];
};

const gridSearch = (matrix, startCoord=[0, 0], endCoord=[matrix.length, matrix[0].length]) => {
    let moves = 0;
    if (checkCoords(matrix, startCoord) && checkCoords(matrix, endCoord)) {
        let queue = [startCoord];
        let queue2 = [];
        let visited = new Set();

        let directions = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]

        while (queue.length) {
            let trend = [];
            const currNode = queue.shift();
            if (visited.has(getCoordStr(currNode))) {
                continue;
            }

            visited.add(getCoordStr(currNode));
            matrix[currNode[0]][currNode[1]] = '█';
            moves++;

            if (currNode[0] == endCoord[0] && currNode[1] == endCoord[1]) return [true, matrix.map(i => i.map(j => j.toString())), moves];
            // up: 0; right: 1; down: 2, left: 3
            // Look down
            if (currNode[0] < endCoord[0]) trend.push(2)
            // Look up
            if (currNode[0] > endCoord[0]) trend.push(0)
            // Look right
            if (currNode[1] < endCoord[1]) trend.push(1)
            // Look left
            if (currNode[1] > endCoord[1]) trend.push(3)
            
            for (let [i, d] of directions.entries()) {
                let newNode = [currNode[0] + d[0], currNode[1] + d[1]];

                if (checkCoords(matrix, newNode)) {
                    if (trend.includes(i)) queue.unshift(newNode); // higher priority
                    else queue.push(newNode); // lower priority
                }
            }
            console.log('Node:',currNode,'Queue:',queue);
        }
    }

    return [false, matrix.map(i => i.map(j => j.toString())), moves];
};


/*
1,1,0,1,1,0,0,
0,1,█,0,0,0,1,
0,1,█,█,1,1,1,
1,1,█,█,█,█,█,
1,1,█,1,1,█,1,
█,█,█,█,1,█,█,
█,1,1,█,█,█,1,
█,█,█,█,1,█,█,
█,█,█,█,█,1,█,
0,1,█,1,1,1,1,
0,0,█,█,0,0,0,
1,1,0,0,0,1,1
*/


/*
1,1,0,1,1,0,0,
0,1,0,0,0,0,1,
0,1,0,0,1,1,1,
1,1,0,0,0,0,0,
1,1,0,1,1,0,1,
0,0,0,0,1,0,0,
0,1,1,█,0,0,1,
0,0,█,█,1,0,0,
0,0,█,0,0,1,0,
0,1,█,1,1,1,1,
0,0,█,█,█,0,0,
1,1,█,█,█,1,1
*/

/*
1,1,0,1,1,0,0,
0,1,0,0,0,0,1,
0,1,0,0,1,1,1,
1,1,0,0,0,0,0,
1,1,0,1,1,0,1,
0,0,0,█,1,0,0,
0,1,1,█,█,0,1,
0,0,█,█,1,0,0,
0,0,█,█,0,1,0,
0,1,█,1,1,1,1,
0,0,█,█,0,0,0,
1,1,0,0,0,1,1 
*/

const gridGenerator = (rows=Math.floor(Math.random() * (20 - 2) + 2), cols=Math.floor(Math.random() * (20 - 2) + 2)) => {
    let output_grid = [];

    for (let y = 0; y < rows; y++) {
        let row = [];
        for (let x = 0; x < cols; x++) {
            chance = Math.random();
            row.push(chance < 0.5 ? 0 : 1);
        }
        output_grid.push(row);
    }
    return output_grid;
};

/*
let grid = [
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1]
];
*/
let grid = [
  [1, 1, 0, 1, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 1],
  [0, 1, 0, 0, 1, 1, 1],
  [1, 1, 0, 0, 0, 0, 0],
  [1, 1, 0, 1, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 1, 1]
]
//grid = gridGenerator();
start_y = Math.floor(Math.random() * ((grid.length - 1) - 2) + 2);
start_x = Math.floor(Math.random() * ((grid[0].length - 1) - 2) + 2);
dest_y = Math.floor(Math.random() * ((grid.length - 1) - 2) + 2);
dest_x = Math.floor(Math.random() * ((grid[0].length - 1) - 2) + 2);

console.log('Starting grid:');

console.log(grid.map(i => i.toString()));

// console.log(`Looking for path from [6, 3] to [10, 3]`)
// let res = gridSearch(grid, [6, 3], [10, 3]);
// console.log(res[0] ? `Path from [6, 3] to [10, 3] is possible: ${res[1].map(i => '\n' + i.toString())}` : 'Path not possible.', `\nPerformed ${res[2]} moves.`);

console.log(`Looking for path from [${start_y},${start_x}] to [${dest_y},${dest_x}]`)
let res = gridSearch(grid, [start_y, start_x], [dest_y, dest_x]);
console.log(res[0] ? `Path from [${start_y},${start_x}] to [${dest_y},${dest_x}] is possible: ${res[1].map(i => '\n' + i.toString())}` : 'Path not possible.', `\nPerformed ${res[2]} move${(res[2] == 1 ? '' : 's')}.`);


let graph = {
    'A' : ['B', 'C', 'D', 'E', 'H', 'I', 'K'],
    'B' : ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'C' : ['A', 'F', 'G', 'I', 'J'],
    'D' : ['C', 'F', 'G', 'I', 'J'],
    'E' : ['B', 'C', 'D', 'F', 'H', 'I', 'J'],
    'F' : ['A', 'B', 'C', 'D', 'E', 'H', 'I', 'J'],
    'G' : ['A', 'B', 'F', 'H', 'I', 'J'],
    'H' : ['B', 'C', 'E', 'F', 'G', 'I'],
    'I' : ['B', 'E', 'F', 'G', 'J'],
    'J' : ['A', 'B', 'E', 'F', 'G', 'I'],
    'K' : ['A', 'L'],
    'L' : ['M'],
    'M' : ['N'],
    'N' : ['A']
};

const getEdges = (graph) => {
    let edges = [];
    for (let nodeA in graph) {
        for (let i = 0; i < graph[nodeA].length; i++) {
            edges.push([nodeA, graph[nodeA][i]]);
        }
    }
    return edges;
};


const buildGraph = (edges) => {
    let g = {};
    for (let e = 0; e < edges.length; e++) {
        let nodeA = edges[e][0];
        let nodeB = edges[e][1];
        if (g[nodeA] == undefined) g[nodeA] = [];
        if (g[nodeB] == undefined) g[nodeB] = [];
        g[nodeA].push(nodeB);
    }
    return g;
};

const findShortestPath = (edges, nodeA, nodeB) => {
    // get a an adjacency list of the edges in the graph
    const graph = buildGraph(edges);
    // keep a record of the nodes we've already considered
    const visited = new Set([nodeA]);
    // keep a record of the nodes and their distance from the starting node
    const queue = [[nodeA, 0]];

    // iterate over the queue to explore all connected nodes
    while (queue.length) {
        // take the first element off the top of the queue and return its values
        const [node, distance] = queue.shift();

        // if we've reached our target node, return how far we traveled
        if (node === nodeB) return distance;

        // let's explore all the neighbors
        for (let neighbor of graph[node]) {
            // if the neighbor hasn't been visited...
            if (!visited.has(neighbor)) {
                // record that we visited this neighbor
                visited.add(neighbor);
                // put the neighbor on the end of the stack, and increase the distance
                queue.push([neighbor, distance+1]);
            }
        }
    }
    // we couldn't get there, so return -1
    return -1;
};

//console.log(buildGraph(getEdges(graph)));
console.log('Shortest path:', findShortestPath(getEdges(graph), 'M', 'A'));


// remove islands that aren't attached to the border
// 1 = land, 0 = water

var matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
];

const checkSurroundings = (matrix, row, col) => {
    let queue = [[row, col]];
    let visited = new Set();

    while (queue.length) {
        const [r, c] = queue.shift();

        if (visited.has(r + ',' + c)) continue;

        visited.add(r + ',' + c);

        let directions = [
            [r - 1, c], // up
            [r + 1, c], // dn
            [r, c - 1], // left
            [r, c + 1]  // right
        ];

        for (const d of directions) {
            // if direction is out of bounds, node is a zero, or we've visited node before, skip it
            if (d[0] < 0 || d[0] >= matrix.length || d[1] < 0 || d[1] >= matrix[0].length || matrix[d[0]][d[1]] == 0 || visited.has(d[0] + ',' + d[1])) continue;

            if (d[0] == 0 || d[0] == matrix.length - 1 || d[1] == 0 || d[1] == matrix[0].length - 1) return true;

            queue.unshift(d);
        }
    }
    return false;
};

// remove islands (adjacent nodes consisting of 1s) which are not connected to the edges
const removeIslands = (matrix) => {
    let o = [...matrix];
    let edgeConnected = false;

    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[0].length; col++) {
            // ignore edges
            if (row == 0 || row == matrix.length - 1) break;
            if (col == 0 || col == matrix[0].length - 1) continue;
            if (matrix[row][col] == 0) continue;

            edgeConnected = checkSurroundings(matrix, row, col);
            if (edgeConnected) continue;

            o[row][col] = 0;
        }
    }
    return o;
};

console.log(removeIslands(matrix));
