/*
validate_node ( graph, node_to_look_at ) {
    (check if node_to_look_at is out of bounds): return false;
    (check if node_to_look_at value == 1): return false;
    return true;
}
    

findpath ( graph, start[y, x], end[y, x] ) {
    // write the base cases
    if (graph doesn't have a size that contains at least two elements): return false;
    if (start is out of bounds): return -1;
    if (end is out of bounds): return -1;
    if (start.value == 1): return -1;
    if (start == end): return 0;

    // make a record of nodes we've visited so we can avoid visiting more than once
    let visited = new Set();
    visited.add(start); // we're visiting this first node immediately

    // instantiate a queue
    let q = [start];

    // start recording distance
    let dist == 0;

    //make record of possible directions
    let dirs = [
        // up, dn, l, r
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
];

    while (q.length) {
        let current = q.shift();

        // look in all directions around the current node
        for d in dirs {
            // compare against the node we're looking at
            // add the [y,x] values of direction to our current node
            look = [current[0] + d[0], current[1] + d[1]]

        // make sure we aren't evaluating an already visited node
        if (visited.has(look)): continue

// add this node to our visited set
visited.add(look)

            if (!validate_node(graph, look)): continue

            if (look[0] == end[0] && look[1] == end[1]): return dist

        q.unshift(look)
        dist++
}
    }
}
*/
const validate_node = (graph, node) => {
    if (node[0] >= graph.length || node[0] < 0 || node[1] >= graph[0].length || node[1] < 0) return false;
    if (graph[node[0]][node[1]] == 1) return false;
    return true;
};


const findPath = (graph, start, end) => {
    // if the graph is invalid
    if (!graph.length >= 2) return false;
    // if either start or end are out of bounds or an obstacle
    if (!validate_node(graph, start) || !validate_node(graph, end)) return -1;
    // if start and end are the same
    if (start[0] + ',' + start[1] == end[0] + ',' + end[1]) return 0;

    // make a record of nodes we've visited so we can avoid visiting more than once
    let visited = new Set();
    visited.add(start[0] + ',' + start[1]); // we're visiting this first node immediately

    graph[start[0]][start[1]] = 9;

    // instantiate a queue
    let q = [start];

    // start recording distance
    let dist = 0;

    while (q.length) {
        const [row, col] = q.shift();

        //make record of possible directions
        let dirs = [
            // up, dn, l, r
            [row - 1, col],
            [row + 1, col],
            [row, col - 1],
            [row, col + 1]
        ];

        // look in all directions around the current node
        for (const d of dirs) {
            // compare against the node we're looking at
            // add the [y,x] values of direction to our current node
            let look = [d[0], d[1]];

            // make sure we aren't evaluating an already visited node
            if (visited.has(look[0] + ',' + look[1])) continue;

            if (!validate_node(graph, look)) continue;
            graph[look[0]][look[1]] = 9;

            // add this node to our visited set
            visited.add(look[0] + ',' + look[1]);

            if (look[0] + ',' + look[1] == end[0] + ',' + end[1]) return [graph, dist];

            q.unshift(look);

            dist++;
        }
    }
    return -1;
};


var matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
];

console.log(findPath(matrix, [0,1], [5,1]));


//////
// Grid pattern search
// https://www.hackerrank.com/challenges/the-grid-search/problem
const checkMatch = (pattern, grid, row, col) => {
    for (const [i, r] of pattern.entries()) {
        for (let j = 0; j < r.length; j++) {
            if (row + i >= grid.length || col + j >= grid[0].length || grid[row + i][col + j] != r.charAt(j)) {
                return 'NO';
            }
        }
    }
    return 'YES';
};


const gridSearch = (G, P) => {
    let matched = 'NO';

    for (const [i, row] of G.entries()) {
        for (let j = 0; j < row.length; j++) {
            // if I'm at the start of the pattern, start search
            if (row.charAt(j) == P[0][0]) {
                matched = checkMatch(P, G, i, j);
                if (matched === 'YES') return matched;
            }
        }
    }
    return matched;
};


var search_grid = [
    '7283455864',
    '6731158619',
    '8988242643',
    '3830589324',
    '2229505813',
    '5633845374',
    '6473530293',
    '7053106601',
    '0834282956',
    '4607924137'
]

var search_pattern = [
    '9505',
    '3845',
    '3530'
]

console.log(gridSearch(search_grid, search_pattern))