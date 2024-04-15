// Graph - largest component
const largestComponent = (graph) => {
	const visited = new Set();
	let longest = 0;

	// iteration allows hopping between separated islands
	for (let node in graph) {
		const size = exploreSize(graph, node, visited);
		if (size > longest) longest = size;
	}

	return longest;
};

// traversal code traverses the connected nodes
const exploreSize = (graph, node, visited) => {
	// return false because this might be a cycle
	if (visited.has(node)) return 0;

	// add the current node to the visited list
	visited.add(node);

	// initialize the size.  1 because we're currently on a node.
	let size = 1;

	// iterate the nodes in the graph
	for (let neighbor of graph[node]) {
		size += exploreSize(graph, neighbor, visited);
	}

	return size;
};

// adjacency list
const graph = {
	0: [8, 1, 5],
	1: [0],
	5: [0, 8],
	8: [0, 5],
	2: [3, 4],
	3: [2, 4],
	4: [3, 2]
};

console.log(
	largestComponent(graph)
);