// Graphs
const breadthFirstPrint = (graph, source) => {
	const queue = [ source ];
	while (queue.length > 0) {
		current = queue.shift();
		console.log(current);
		for (let neighbor of graph[current]) {
			queue.push(neighbor);
		}
	}
};

const depthFirstPrint = (graph, source) => {
	const stack = [ source ];

	while (stack.length > 0) {
		const current = stack.pop();
		console.log(current);
		for (let neighbor of graph[current]) {
			stack.push(neighbor);
		}
	}
};

const depthFirstPrintRecursive = (graph, source) => {
	console.log(source);
	for (let neighbor of graph[source]) {
		depthFirstPrintRecursive(graph, neighbor);
	}
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

breadthFirstPrint(graph, 'a');