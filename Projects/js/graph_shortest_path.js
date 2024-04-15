// Graph - shortest path
// must build adjacency list first, as we are only given a list of edges
// breadth-first typically easiest way to calculate shortest path vs depth-first
const shortestPath = (edges, start, end) => {
	const graph = buildGraph(edges);
	// add start node to visited set
	const visited = new Set([start]);
	// start node is zero edges from itself
	const queue = [ [start, 0] ];

	// step through the queue
	while (queue.length > 0) {
		const [node, distance] = queue.shift();

		if (node === end) return distance;

		for (let neighbor of graph[node]) {
			if (!visited.has(neighbor)){
				visited.add(neighbor);
				queue.push([neighbor, distance + 1]);
			}
		}
	}
	// there is no path that connects start to end node
	return -1
};


const buildGraph = (edges) => {
	// create a map to show our node associations
	const graph = {};

	// iterate the edges
	for (let edge of edges) {
		// connect the nodes
		const [ a, b ] = edge;
		// add the nodes to our graph
		if (!(a in graph)) graph[a] = [];
		if (!(b in graph)) graph[b] = [];
		// draw a connection between our two nodes
		graph[a].push(b);
		graph[b].push(a);
	}
	// pass back the completed adjacency list
	return graph;
}

const edges = [
	['w', 'x'],
	['x', 'y'],
	['z', 'y'],
	['z', 'v'],
	['w', 'v']
];

console.log(
	shortestPath(edges, 'w', 'z')
);