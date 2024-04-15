// openersToClosers
const isValid = (code) => {
	const validCodeString = ": This code is valid!";
	const invalidCodeString = ": This code is NOT valid.";
	// init opening and closing character pairs
	const openersToClosers = {
		'(': ')',
		'[': ']',
		'{': '}',
		'<': '>'
	};
	// associate opening and closing chars in their on vars
	const openers = new Set(Object.keys(openersToClosers));
	const closers = new Set(Object.values(openersToClosers));

	let openersStack = [];

	for (let char of code) {
		if (openers.has(char)) {
			openersStack.push(char);
		} else if (closers.has(char)) {
			if (!openersStack.length) {
				return code + invalidCodeString;
			}
			let lastUnclosedOpener = openersStack.pop();

			if (openersToClosers[lastUnclosedOpener] !== char) {
				return code + invalidCodeString;
			}
		}
	}
	return code + validCodeString;
}

console.log(isValid('[]([]][()()[[[[]'));
console.log(isValid('([](<[{}]>))'));
console.log(isValid('<*))))><'));