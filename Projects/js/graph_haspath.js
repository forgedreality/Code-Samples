// Graph - has path
// time = edges
// space = nodes
const hasPathBreadthFirst = (graph, src, dst) => {
	const queue = [src];

	while (queue.length > 0) {
		const current = queue.shift();
		if (current === dst) return true;

		for (let neighbor of graph[current]) {
			queue.push(neighbor);
		}
	}
	return false;
};

const hasPath = (graph, src, dst) => {
	if (src === dst) return true;

	for (let neighbor of graph[src]) {
		if (hasPath(graph, neighbor, dst) === true) {
			return true;
		}
	}

	return false;
};

// Adjacency list
const graph = {
	a: ['b', 'c'],
	b: ['d'],
	c: ['e'],
	d: ['f'],
	e: [],
	f: []
}

console.log(hasPathBreadthFirst(graph, 'a', 'd'));