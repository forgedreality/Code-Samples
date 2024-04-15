// Graph - undirected
const undirectedPath = (edges, nodeA, nodeB) => {
	const graph = buildGraph(edges);
	return hasPath(graph, nodeA, nodeB, new Set());
}

// see if we can find a path from nodeA to nodeB
const hasPath = (graph, src, dst, visited) => {
	// if we're at the destination, we're done!
	if (src === dst) return true;
	// if we've previously visited this node, we completed a cycle, so let's stop iterating
	if (visited.has(src)) return false;

	// make sure we add this node to our visited list
	visited.add(src);

	for (let neighbor of graph[src]) {
		// check if the current neighbor completes the path
		if (hasPath(graph, neighbor, dst, visited) === true) {
			return true;
		}
	}

	// we couldn't find a path to the destination
	return false;
}

// build adjacency list from edge list
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
	['i', 'j'],
	['k', 'i'],
	['m', 'k'],
	['k', 'l'],
	['o', 'n']
];

console.log(undirectedPath(edges, 'i', 'k'));