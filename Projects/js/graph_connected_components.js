// Graph - connected components count
const connectedComponentsCount = (graph) => {
	const visited = new Set();
	let count = 0;

	for (let node in graph) {
		if (explore(graph, node, visited) === true) {
			count += 1;
		}
	}

	return count;
};

const explore = (graph, current, visited) => {
	// return false because this might be a cycle
	if (visited.has(String(current))) return false;

	// add the current node to the visited list
	visited.add(String(current));

	// iterate the nodes in the graph
	for (let neighbor of graph[current]) {
		explore(graph, neighbor, visited);
	}

	return true;
};

console.log(
	connectedComponentsCount({
		0: [8, 1, 5],
		1: [0],
		5: [0, 8],
		8: [0, 5],
		2: [3, 4],
		3: [2, 4],
		4: [3, 2]
	})
);