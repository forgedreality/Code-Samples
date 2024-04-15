function * test() {
    yield 1;
    yield 2;
    yield true;
}

const a = test();
a.next();
const x = a.next();
a.next();
console.log(x);

// shortest array of repeating numbers; allows for multiple (ie, if more than one number repeats the same number of times)
const solution = (numbers) => {
    let l = numbers.length;
    let hash = new Map();

    for (let i = 0; i < l; i++) {
        if (hash.has(numbers[i])) {
            hash.set(numbers[i], hash.get(numbers[i]) + 1);
        } else { 
            hash.set(numbers[i], 1);
        }
    }

    let min_count = l + 1
    let res = [];

    hash.forEach((v, k) => {
        if (min_count >= v) {
            res.push(k);
            min_count = v;
        }
    });

    return res.sort();
};

console.log(solution([10, 10, 941, 13, 13, 13, 941]))

// merge sort
const solution2 = (array) => {
    function merge(left, right) {
      let merged = [];

      while (left.length && right.length) {
        if (left[0] < right[0]) {
            merged.push(left.shift());
        } else {
            merged.push(right.shift());
        }
      }

      return [...merged, ...left, ...right];
    }

    function mergeSort(array) {
      let m = [];
      if (array.length <= 1) {
        return array;
      }

      let middleIndex = Math.floor(array.length / 2);

      let left = array.slice(0, middleIndex);
      let right = array.slice(middleIndex, array.length);

      return merge(mergeSort(left), mergeSort(right));
    }

    return mergeSort(array);
};

console.log(solution2([1,2,3,4,50,23,10,75,30,-12,100,75,10]));

// longest repeating string
const solution3 = (n) => {
    let o = n.toString();
    let longest = '';
    let chrs = '';

    for (let i = 0; i < o.length; i++) {
        if (i == 0) {
            if (o[i] === o[i + 1]) {
                chrs += o[i];
            }
        }
        if (i > 0) {
            if (o[i] === o[i - 1]) {
                chrs += o[i];
            }
            if (o[i] !== o[i - 1]) {
                chrs = o[i];
            }
            if (chrs.length > longest.length) {
                longest = chrs;
            }
        }
    }
    return parseInt(longest, 10);
};

console.log(solution3(411079718950849));

// longest non-repeating string
const solution4 = (numbers) => {
    let o = numbers.toString();
    let longest = 0;

    for (let i = 0; i < o.length; i++) {
        let curr_str = new Set();

        for (let j = i; j < o.length; j++) {
            if (curr_str.has(o[j])) {
                break;
            } else {
                curr_str.add(o[j]);
            }
        }

        longest = Math.max(longest, curr_str.size);
    }

    return longest;
}

console.log(solution4(1123223));


const messageSolution = (messages) => {
  class Emitter {
    constructor(messages = []) {
      this.messages = messages;
      this.event = () => {};
    }

    setEvent(fn) {
      this.event = fn;
    }

    trigger() {
      this.messages.forEach(message => this.event);
    }
  }

  class Receiver {
    constructor() {
      this.messages = [];
    }

    ping(message) {
      this.messages.push(message);
    }
  }

  const myEmitter = new Emitter(messages);
  const myReceiver = new Receiver();

  myEmitter.setEvent(myReceiver.ping(messages));
  myEmitter.trigger();

  return myReceiver.messages[0];
};

console.log(messageSolution(["A", "B", "C"]))
