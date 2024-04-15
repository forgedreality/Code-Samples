// balanced brackets
// FINISHED?
/*const solution = (angles) => {
    let openers = [];
    let closers = [];
    let balance = 0;
    let out = angles;

    for (let i = 0; i < angles.length; i++) {
        let curr = angles.charAt(i);

        balance = openers.length - closers.length;

        if (curr == '<') {
            openers.push(curr);
        }
        else {
            if (balance < 1) out = '<' + out;
            else closers.push(curr);
        }
    }

    for (let x = 0; x <= balance; x++) {
        out = out + '>';
    }

    return out;
}
*/


const solution = (angles) => {
    // used for tracking balance of opens and closes
    let balance = 0;
    // set up a queue to step through
    let queue = angles.split('');

    while (queue.length) {
        // get our current character from the front of the queue
        curr = queue.shift();
        // add or subtract 1 based on whether it's an open or close
        // to keep track of our balance. This will be used later to
        // determine how many closers we need at the end of our string.
        balance += curr == '<' ? 1 : -1;

        // check if we're out of balance
        // if we've gone below zero, we have too many closers so far
        // maybe a while loop would work better
        if (balance < 0) {
            // add an open to the start
            angles = '<' + angles;
            // adjust balance to reflect change
            balance += 1;
        }
    }

/*
    let queue = 0;
    let len = angles.length - 1;
    while (queue < len) {
        let char = angles.charAt(queue);
        balance += char == '<' ? 1 : -1;

        if (balance < 0) {
            angles = '<' + angles;
            balance += 1;
        }

        queue++;
    }
*/
/*
    // there is probably a more elegant way to do this, but we need
    // to add the closers after the while loop, or it can add too many
    // *deprecated
    while (balance > 0) {
        // add one for each character imbalance
        closers += '>';
        balance--;
        console.log(balance, closers);
    }
*/
    return angles + '>'.repeat(Math.abs(balance));
};

// console.log(Array(8).fill().map(_ => (Math.random() > 0.5 ? '<' : '>')).join(''));

// get a random length string of < and >
//                              :Random length if not provided                        :convert to base 2 and remove first 2 chars :replace 0 and 1 with > and <
const generateRandomBrackets = (length=(1 + Math.random() * (69 - 1)))=> Math.random().toString(2).substr(2, length).replaceAll('0', '<').replaceAll('1', '>');
brackets = generateRandomBrackets();

// brackets = '<>>>>>><';

console.log('Input brackets:', brackets);
console.log(solution(brackets));

