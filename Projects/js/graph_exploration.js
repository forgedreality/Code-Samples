const findShortestPath = (edges, nodeA, nodeB) => {
	// get a an adjacency list of the edges in the graph
	const graph = buildGraph(edges);
	// keep a record of the nodes we've already considered
	const visited = new Set([nodeA]);
	// keep a record of the nodes and their distance from the starting node
	const queue = [[nodeA, 0]];

	// iterate over the queue to explore all connected nodes
	while (queue.length > 0) {
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


// create adjacency list
const buildGraph = (edges) => {
	// declare the graph object
	const graph = {};

	// iterate over each input edge
	for (let edge of edges) {
		// init the nodes
		const [a, b] = edge;
		// add the nodes to our graph if not already present
		if (!(a in graph)) graph[a] = [];
		if (!(b in graph)) graph[b] = [];
		// draw a connection between our two nodes
		graph[a].push(b);
		graph[b].push(a);
	}
	// pass back the result
	return graph;
};

const edges = [
	['A','B'],
	['A','D'],
	['B','E'],
	['E','F'],
	['F','C'],
	['C','G'],
	['G','E']
];

console.log(findShortestPath(edges, 'A', 'G'));