// TODO: Add functionality for shorthand code snippets within textarea elements.
// Look for ':' and replace if preceding characters (until a space or some character limit) are a match for a macro.
// ex: typing 'pyfor:' inserts a boilerplate Python for statement code block.
// The following returns TRUE if currently focused element is a textarea or input element:
// !!~[].indexOf.call(document.querySelectorAll("input, textarea"), document.activeElement)

let selTag = '¡';
let perform = false;
let selections = [];
let sel = 0;
let content = '';
// character to trigger macro replace
let triggerChr = ':';

const tag = (str) => {
  return selTag + str + selTag;
};

const getTriggers = () => {
  let list = `POSSIBLE MACROS:\n`;
  for (const p in macroTriggers) {
    list += ` ${p}\n`;
  }
  return list;
};

function getQuote() {
  let quotes = [
    `"The greatest glory in living lies not in never falling, but in rising every time we fall." -Nelson Mandela`,
    `"The way to get started is to quit talking and begin doing." -Walt Disney`,
    `"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking." -Steve Jobs`,
    `"If life were predictable it would cease to be life, and be without flavor." -Eleanor Roosevelt`,
    `"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough." -Oprah Winfrey`,
    `"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success." -James Cameron`,
    `"Life is what happens when you're busy making other plans." -John Lennon`,
    `"Spread love everywhere you go. Let no one ever come to you without leaving happier." -Mother Teresa`,
    `"When you reach the end of your rope, tie a knot in it and hang on." -Franklin D. Roosevelt`,
    `"Always remember that you are absolutely unique. Just like everyone else." -Margaret Mead`,
    `"Don't judge each day by the harvest you reap but by the seeds that you plant." -Robert Louis Stevenson`,
    `"The future belongs to those who believe in the beauty of their dreams." -Eleanor Roosevelt`,
    `"Tell me and I forget. Teach me and I remember. Involve me and I learn." -Benjamin Franklin`,
    `"The best and most beautiful things in the world cannot be seen or even touched — they must be felt with the heart." -Helen Keller`,
    `"It is during our darkest moments that we must focus to see the light." -Aristotle`,
    `"Whoever is happy will make others happy too." -Anne Frank`,
    `"Do not go where the path may lead, go instead where there is no path and leave a trail." -Ralph Waldo Emerson`,
    `"You will face many defeats in life, but never let yourself be defeated." -Maya Angelou`,
    `"The greatest glory in living lies not in never falling, but in rising every time we fall." -Nelson Mandela`,
    `"In the end, it's not the years in your life that count. It's the life in your years." -Abraham Lincoln`,
    `"Never let the fear of striking out keep you from playing the game." -Babe Ruth`,
    `"Life is either a daring adventure or nothing at all." -Helen Keller`,
    `"Many of life's failures are people who did not realize how close they were to success when they gave up." -Thomas A. Edison`,
    `"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose." -Dr. Seuss`,
    `"Keep smiling, because life is a beautiful thing and there's so much to smile about." -Marilyn Monroe`,
    `"Life is a long lesson in humility." -James M. Barrie`,
    `"In three words I can sum up everything I've learned about life: it goes on." -Robert Frost`,
    `"Love the life you live. Live the life you love." -Bob Marley`,
    `"Life is either a daring adventure or nothing at all." -Helen Keller`,
    `"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose." -Dr. Seuss`,
    `"Life is made of ever so many partings welded together." -Charles Dickens`,
    `"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma — which is living with the results of other people's thinking." -Steve Jobs`,
    `"Life is trying things to see if they work." -Ray Bradbury`,
    `"Many of life's failures are people who did not realize how close they were to success when they gave up." -Thomas A. Edison`,
    `"Success is not final; failure is not fatal: It is the courage to continue that counts." -Winston S. Churchill`,
    `"Success usually comes to those who are too busy to be looking for it." -Henry David Thoreau`,
    `"The way to get started is to quit talking and begin doing." -Walt Disney`,
    `"If you really look closely, most overnight successes took a long time." -Steve Jobs`,
    `"The secret of success is to do the common thing uncommonly well." -John D. Rockefeller Jr.`,
    `"I find that the harder I work, the more luck I seem to have." -Thomas Jefferson`,
    `"The real test is not whether you avoid this failure, because you won't. It's whether you let it harden or shame you into inaction, or whether you learn from it; whether you choose to persevere." -Barack Obama`,
    `"You miss 100% of the shots you don't take." -Wayne Gretzky`,
    `"Whether you think you can or you think you can't, you're right." -Henry Ford`,
    `"I have learned over the years that when one's mind is made up, this diminishes fear." -Rosa Parks`,
    `"I alone cannot change the world, but I can cast a stone across the water to create many ripples." -Mother Teresa`,
    `"Nothing is impossible, the word itself says, 'I'm possible!'" -Audrey Hepburn`,
    `"The question isn't who is going to let me; it's who is going to stop me." -Ayn Rand`,
    `"The only person you are destined to become is the person you decide to be." -Ralph Waldo Emerson`
  ];

  let q = Math.floor(Math.random() * quotes.length);
  return quotes[q];
}

// note: keep keys shorter than 10 chars.
const macroTriggers = {
    "e1"         : `forgedreality@gmail.com`,
    "e2"         : `synergyforge@gmail.com`,
    "e3"         : `forgedreality@comcast.net`,
    "e4"         : `forged-reality@comcast.net`,
    "li"         : `https://www.linkedin.com/in/forgedreality`,
    "gh"         : `https://github.com/forgedreality`,
    "p"          : `425.351.7453`,
    "info"       : `As a multi-faceted, self-taught developer and a general jack-of-all-trades, I am not afraid to venture into unfamiliar territory.  I am quite good at quickly learning new disciplines and technologies.  I enjoy learning from, as well as mentoring others.  I often find myself writing programs to improve my productivity or to simplify repetitive tasks by leveraging technologies such as REST APIs, Python applications, and custom web browser extensions.  When I put my mind to it, nothing is outside my comfort zone, and I am excited to bring my expertise and willingness to improve to the right team.`,
    // Zulily
    "j1c"        : `Zulily`,
    "j1t"        : `UI Developer - Email Production`,
    "j1"         : `* Key member of the Outbound Marketing team, driving 50% of company revenue, and managing a database of 110M customers\n* Owner of email templates as well as Outbound data and site connections - ensuring templates, data and site unify to provide personalized communications to 15M+ customers daily\n* Primary contact bridging marketing and engineering teams, ideating and executing on mutually beneficial programs and ensuring priorities for both teams move forward\n* Execute improvements to critical campaigns (Gmail clipping, dark mode support) driving an incremental $10M in annual revenue\n* Improve personalization, data hygiene, and enhanced templates to incorporate best practices and increase deliverability\n* Primary Outbound developer working on a dual migration from legacy e-commerce and engagement platforms to Shopify and Iterable; executed migration ahead of schedule, within 4 months`,
    // PeopleConnect
    "j2c"        : `PeopleConnect`,
    "j2t"        : `Senior Software Engineer`,
    "j2"         : `* Conceptualized and built dynamic, stackable email content blocks based on marketable user data, metrics, and collaborative input from cross-functional teams\n* Led onboarding training and provided mentorship for a team of 6 remote developers, transitioning to the new stewards of email platform, providing a $500k yearly reduction in staff costs\n* Acted as resident Git/SVN guru and release coordinator, helping the team to embrace better branching strategies, reduce code conflicts, and streamlining workflows and code review`,
    // Classmates.com
    "j3c"        : `Classmates.com`,
    "j3t"        : `Software Engineer`,
    "j3"         : `* Spearheaded front-end transition to a fully customizable, in-house B2C email framework sending more than 12M unique emails per day, which drives 90% of daily site traffic\n* Built QA, testing, and prototyping tools, leveraging Java, Spring, and Freemarker to promote rapid development life cycles`,
    // ADP Dealer Services
    "j4c"        : `ADP Dealer Services`,
    "j4t"        : `Software Engineer`,
    "j4"         : `* Managed B2B email development, testing, scheduling, and reporting, sending up to 8M emails per day\n* Provided support and testing for web and mobile application`,
    // The Cobalt Group
    "j5c"        : `The Cobalt Group`,
    "j5t"        : `Web Content Developer`,
    "j5"         : `* Utilized JavaScript, PHP, and HTML to create robust, efficient content for multiple B2B websites\n* Tested web and mobile application functionality, providing end-to-end QA support`,
    "html"       : `<!DOCTYPE html>\n<html lang=\"en\">\n  <head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">\n    <title>${tag('HTML 5 Boilerplate')}</title>\n    <link rel=\"stylesheet\" href=\"${tag('style.css')}\">\n  </head>\n  <body>\n    ${tag('<script src=\"index.js\"></script>')}\n  </body>\n</html>\n`,
    "pyfor"      : `for ${tag('x')} in ${tag('y')}:\n    ${tag('')}`,
    "pyfor2"     : `for ${tag('x')},${tag('y')} in enumerate(${tag('object')}):\n    ${tag('')}`,
    "pytwosum"   : `def twosum(target, nums):\n    out = []\n    for i in nums:\n        comp = target - i\n        if comp in nums:\n            out.extend([comp, i])\n            return out\n    return \'Not found\'\n\nprint(twosum(23, [4, 17, 6, 12, 5, 9, 2, 1, 48, 19, 27, 8, 7, 10, 15]))`,
    "pyshortest" : `def findShortestPath(edges, nodeA, nodeB):\n    # get an adjacency list of the edges in the graph\n    graph = buildGraph(edges)\n    # keep a record of the nodes we've already considered\n    visited = {nodeA}\n     # keep a record of the nodes and their distance from the starting node\n    queue = [[nodeA, 0]]\n\n    # iterate over the queue to explore all connected nodes\n    while len(queue) > 0:\n        # take the first element off the top of the queue and return its values\n        [node, distance] = popfirst(queue)\n\n        # if we've reached our target node, return how far we traveled\n        if node == nodeB: return distance\n\n        # let's explore all the neighbors\n        for neighbor in graph[node]:\n            # if the neighbor hasn't been visited...\n            if neighbor not in visited:\n                # record that we visited this neighbor\n                visited.add(neighbor)\n                # put the neighbor on the end of the stack, and increase the distance\n                queue.append([neighbor, distance+1])\n\n    # we couldn't get there, so return -1\n    return -1\n\n\n# create adjacency list\ndef buildGraph(edges):\n    # declare the graph object\n    graph = {}\n\n    # iterate over each input edge\n    for edge in edges:\n        # init the nodes\n        [a, b] = edge\n        # add the nodes to our graph if not already present\n        if a not in graph: graph[a] = []\n        if b not in graph: graph[b] = []\n\n        # draw a connection between our two nodes\n        graph[a].append(b);\n        graph[b].append(a);\n\n    # pass back the result\n    return graph;\n\nedges = [\n    ['A','B'],\n    ['A','D'],\n    ['B','E'],\n    ['E','F'],\n    ['F','C'],\n    ['C','G'],\n    ['G','E']\n]\n\nprint(findShortestPath(edges, 'A', 'G'))\n`,
    "jsfor"      : `for (let i = 0; i < 0; i++) {\n    ${tag('code goes here')}\n}`,
    "jstwosum"   : `const twoSum = (target, nums) => {\n    let out = [];\n    for (let i = 0; i < nums.length; i++) {\n        let comp = target - nums[i];\n        if (comp in nums) {\n            out.push(comp, nums[i])\n            return out;\n        }\n    }\n    return \"Not found\";\n};\n//console.log(twoSum(23, [4, 17, 6, 12, 5, 9, 2, 1, 48, 19, 27, 8, 7, 10, 15]));\n`,
    "jsshortest" : `const findShortestPath = (edges, nodeA, nodeB) => {\n    // get a an adjacency list of the edges in the graph\n    const graph = buildGraph(edges);\n    // keep a record of the nodes we've already considered\n    const visited = new Set([nodeA]);\n    // keep a record of the nodes and their distance from the starting node\n    const queue = [[nodeA, 0]];\n\n    // iterate over the queue to explore all connected nodes\n    while (queue.length > 0) {\n        // take the first element off the top of the queue and return its values\n        const [node, distance] = queue.shift();\n\n        // if we've reached our target node, return how far we traveled\n        if (node === nodeB) return distance;\n\n        // let's explore all the neighbors\n        for (let neighbor of graph[node]) {\n            // if the neighbor hasn't been visited...\n            if (!visited.has(neighbor)) {\n                // record that we visited this neighbor\n                visited.add(neighbor);\n                // put the neighbor on the end of the stack, and increase the distance\n                queue.push([neighbor, distance+1]);\n            }\n        }\n    }\n    // we couldn't get there, so return -1\n    return -1;\n};\n\n// create adjacency list\nconst buildGraph = (edges) => {\n    // declare the graph object\n    const graph = {};\n\n    // iterate over each input edge\n    for (let edge of edges) {\n        // init the nodes\n        const [a, b] = edge;\n        // add the nodes to our graph if not already present\n        if (!(a in graph)) graph[a] = [];\n        if (!(b in graph)) graph[b] = [];\n        // draw a connection between our two nodes\n        graph[a].push(b);\n        graph[b].push(a);\n    }\n    // pass back the result\n    return graph;\n};\n\nconst edges = [\n    ['A','B'],\n    ['A','D'],\n    ['B','E'],\n    ['E','F'],\n    ['F','C'],\n    ['C','G'],\n    ['G','E']\n];\n\nconsole.log(findShortestPath(edges, 'A', 'G'));\n`,
    "quote" : `getQuote`
};

macroTriggers["help"] = getTriggers();

/*
// ability to get path to content for different websites
const inputObjects = (element) => {
  var o = element;

  const contentMap = {
      // discord
      'markup-eYLPri' : element.childNodes[0].childNodes[0].childNodes[0].childNodes[0],
      // twitch
      'chat-wysiwyg-input__editor' : element.childNodes[0].childNodes[0].childNodes[0].childNodes[0]
  };

  (() => {
    let c = element.className;

    for (const k of Object.keys(contentMap)) {
      if (c.includes(k)) {
        o = contentMap[k];
      }
    }
  })();

  return o;
};
*/

function createSelection(inputText, start, end) {
  if (inputText.tagName == 'DIV') {
    let temp = new Range();
    temp.setStart(inputText.firstChild, start);
    temp.setEnd(inputText.firstChild, end);

    let textNode = inputText.childNodes[0]; //text node is the first child node of a div

    let r = document.createRange();
    let startIndex = 0;
    let endIndex = textNode.textContent.length;
    r.setStart(textNode, start);
    r.setEnd(textNode, end);

    let s = window.getSelection();
    s.removeAllRanges();
    s.addRange(r);
  }

  else {
    if (inputText.createTextRange) {
      let selRange = inputText.createTextRange();
      selRange.collapse(true);
      selRange.moveStart('character', start);
      selRange.moveEnd('character', end - start);
      selRange.select();
    }

    else if (inputText.setSelectionRange) {
      inputText.focus();
      inputText.setSelectionRange(start, end);
    }

    else if (typeof inputText.selectionStart != 'undefined') {
      inputText.selectionStart = start;
      inputText.selectionEnd = end;
      inputText.focus();
    }
  }
}

const getCursorPos = (input) => {
  let caretOffset = 0;

  if (input.tagName == 'DIV') {
    let doc = input.ownerDocument || input.document;
    let win = doc.defaultView || doc.parentWindow;
    let selRange;
    if (typeof win.getSelection != "undefined") {
      selRange = win.getSelection();
      if (selRange.rangeCount > 0) {
        let range = win.getSelection().getRangeAt(0);
        let preCaretRange = range.cloneRange();
        preCaretRange.selectNodeContents(input);
        preCaretRange.setEnd(range.endContainer, range.endOffset);
        caretOffset = preCaretRange.toString().length;
      }
    } else if ((selRange = doc.selection) && selRange.type != "Control") {
      let textRange = selRange.createRange();
      let preCaretTextRange = doc.body.createTextRange();
      preCaretTextRange.moveToElementText(input);
      preCaretTextRange.setEndPoint("EndToEnd", textRange);
      caretOffset = preCaretTextRange.text.length;
    }
  }

  else {
    if ("selectionStart" in input && input.selectionStart) {
      caretOffset = input.selectionStart;
    }

    else if (input.createTextRange) {
      let selRange = document.selection.createRange();
      if (selRange.parentElement() === input) {
        let rng = input.createTextRange();
        rng.moveToBookmark(selRange.getBookmark());
        for (let len = 0; rng.compareEndPoints("EndToStart", rng) > 0; rng.moveEnd("character", -1)) {
          len++;
        }

        rng.setEndPoint("StartToStart", input.createTextRange());
        for (let pos = {
          start: 0,
          end: len
        }; rng.compareEndPoints("EndToStart", rng) > 0; rng.moveEnd("character", -1)) {
          pos.start++;
          pos.end++;
        }
        caretOffset = pos;
      }
    }
  }
  return caretOffset;
};

const boilerplate = (inputStr, pos) => {
  // pos - 2 because string is zero-based, and one more to go before the last character typed
  // better method?
  let p = pos - 2;
  let str = '';
  var replace = '';
  // let invalid = ' ;:[]/()!@#$%^&*"\'\\\n';

  for (let c = p; c >= 0; c--) {
    let chr = inputStr.charAt(c);

    if (str.length > 10) {
      break;
    }
/*
    if (invalid.includes(chr) || str.length > 10) {
      break;
    }
*/
    str = chr + str;

    if (macroTriggers[str] != undefined) {
      // Object.keys(macroTriggers)[Object.keys(macroTriggers).length - 2] gets the last item in the list of macros that is not 'help'
      // since 'help' gets added last, we skip over that one, and get the name of the second-to-last key in the object; normally 'quote',
      // but the name could change.  As could its position.  Maybe just deciding on a name and not changing it would be better.  That way,
      // it can change position within the object.
      // inputStr = inputStr.slice(0, pos - (str.length + 1)) + (str == Object.keys(macroTriggers)[Object.keys(macroTriggers).length - 2] ? getQuote() : macroTriggers[str]) + inputStr.slice(pos, inputStr.length);
      inputStr = inputStr.slice(0, pos - (str.length + 1)) + (str == 'quote' ? getQuote() : macroTriggers[str]) + inputStr.slice(pos, inputStr.length);
      perform = true;
      sel = 0;
      replace = str + triggerChr;
      break;
    }
  }

  return [inputStr, replace];
};

const getSelections = (text) => {
  selections = [];
  let sl = selTag.length;
  let found = text.indexOf(selTag);

  while (found != -1) {
    let o = [];
    o.push(found);
    found = text.indexOf(selTag, found + sl);
    if (found != -1) {
      let f = found + sl;
      o.push(f);
      selections.push(o);
      found = text.indexOf(selTag, f);
    }
  }

  if (sel > selections.length - 1) sel = 0;
  return selections;
};

const selText = (s, ele) => {
  if (s < selections.length) {
    createSelection(ele, selections[s][0], selections[s][1]);
    sel++;
    if (sel > selections.length - 1) sel = 0;
  }
  return sel;
};

document.body.addEventListener('keydown', function(event){
  let e = document.activeElement;
/*
  //  Get content of active element to support multiple websites, typically for editable divs
  let e_content = inputObjects(e);
  // if the text element is nested, let's make a note of it for later
  let shift_content = e == e_content ? false : true;
*/
  let ele = e.tagName;
  // record the type for current element to refer to later
  let t = e.type;

  if (event.key == 'Tab' && ((!!~[].indexOf.call(document.querySelectorAll("input"), e) && e.type != 'checkbox') || !!~[].indexOf.call(document.querySelectorAll("textarea"), e) || ele == 'DIV')) {
    perform = false;
    let count = selections.length;
    //s = ele == 'DIV' ? (shift_content ? e_content.innerHTML : e.innerHTML) : (shift_content ? e_content.value : e.value);
    s = ele == 'DIV' ? e.innerHTML : e.value;

    if (s.includes(selTag)) event.preventDefault();
    if (!(ele == 'DIV') && e.selectionStart == null) {
      // types such as email, date, number do not support selectionStart
      // so we temporarily set to 'text', and change it back when we're done
      e.type = 'text';
      e.selectionStart = e.value.length;
    }

    // let pos = getCursorPos(shift_content ? e_content : e);
    let pos = getCursorPos(e);

    //content = boilerplate(s, pos);
    // if (!e.isContentEditable) content = content.replaceAll('&gt;', '>').replaceAll('&lt;', '<');
    selections = getSelections(ele == 'DIV' ? s.replaceAll('&gt;', '>').replaceAll('&lt;', '<') : s);

    if (selections.length != count) {
      sel = 0;
    }
  }
  //e.type = t;
});

// updates the input instead of simply setting its value
const typeInto = (el, data) => {
  // note the use of the InputEvent constructor
  const e = new InputEvent('input', {
    inputType: 'insertText',
    data
  });

  // manually add the text to element.value
  el.value += data;

  // fire the event
  el.dispatchEvent(e);
};

document.body.addEventListener('keyup', function(event){
  console.log("got here");
  let sl = selTag.length;
  let s = '';
  let o = [];
  let e = document.activeElement;
/*
  //  Get content of active element to support multiple websites, typically for editable divs
  let e_content = inputObjects(e);
  // if the text element is nested, let's make a note of it for later
  let shift_content = e == e_content ? false : true;
*/
  let ele = e.tagName;
  // record the type for current element to refer to later
  let t = e.type;

  if ((!!~[].indexOf.call(document.querySelectorAll("input"), e) && e.type != 'checkbox') || !!~[].indexOf.call(document.querySelectorAll("textarea"), e) || ele == 'DIV') {
    if (event.key == triggerChr) {
      perform = false;
      //  Change active element if it's Discord chat
      //e = e.className.includes('markup-eYLPri') ? e.childNodes[0].childNodes[0].childNodes[0].childNodes[0] : e;

/*
      // Getting div content (for testing)
      const sel = document.getSelection();
      // sel.anchorNode.data = 'testing';
      // input.textContent.trim()
      if (sel.anchorNode != undefined) sel.collapseToEnd();
*/
      // s = (ele == 'DIV') ? e.innerHTML : e.value;
      s = (ele == 'DIV') ? e.textContent : e.value;

      if (!(ele == 'DIV') && e.selectionStart == null) {
        // types such as email, date, number do not support selectionStart
        // so we temporarily set to 'text', and change it back when we're done
        e.type = 'text';
        e.selectionStart = e.value.length;
      }

      let pos = getCursorPos(e);

      let response = boilerplate((ele == 'DIV' ? s.replaceAll('&gt;', '>').replaceAll('&lt;', '<') : s), pos);

      content = response[0].replace(response[1]);
      // if (!e.isContentEditable) content = content.replaceAll('&gt;', '>').replaceAll('&lt;', '<');

      if (perform) {
        if (ele == 'DIV') {
          e.innerHTML = content.replaceAll('>', '&gt;').replaceAll('<', '&lt;');
          // content = e.innerHTML;
          //selStart = activeElement.innerHTML.indexOf(selTag);
          //selEnd = selStart != -1 ? activeElement.innerHTML.indexOf(selTag, selStart) : -1;
        }
        else {
          // e.value = content.replaceAll('>', '&gt;').replaceAll('<', '&lt;');
          // e.value = e.value.replace(response[1], '');
          e.value = '';
          // simulate typing so that the input value actually updates on the form
          content.split('').forEach(letter => { typeInto(e, letter); });

          /* e.value = content; */

          // content = e.value;
          //selStart = e.value.indexOf(selTag);
          //selEnd = selStart != -1 ? e.value.indexOf(selTag, selStart + sl) + sl : -1;
        }

        // Select a portion of text
        selections = getSelections((ele == 'DIV') ? content.replaceAll('&gt;', '>').replaceAll('&lt;', '<') : (e.type == 'text' ? content.replaceAll('\n', '') : content));
        sel = selText(sel, e);
      }
    }

    else if (event.key == 'Tab') {
      if (e.selectionStart == null) {
        // types such as email, date, number do not support selectionStart
        // so we temporarily set to 'text', and change it back when we're done
        e.type = 'text';
        //e.selectionStart = e.value.length;
      }

      if (selections.length > 0) {
        sel = selText(sel, e);
      }
    }
  }
  e.type = t;
});


// C:\Users\Forged\AppData\Roaming\Mozilla\Firefox\Profiles\glzgu2b4.dev-edition-default\extensions
// start ignoring when we see one of these characters
let pauseStrings = [
  "<"
];

// stop ignoring when we see one of these characters
let unpauseStrings = [
  ">"
];

// ignore all content between these characters... (1/2)
let blockStart = [
  "╔",
  "╕",
  "╖",
  "╗"
];

// and these characters.  This allows code snippets and commented HTML to be ignored entirely. (2/2)
let blockEnd = [
  "╘",
  "╙",
  "╚",
  "╛"
];

// ignore characters while this is true
let pause = false;
// toggle ignoring blocks of code while this is true
let blockPause = false;
// keep characters from swapping positions
let preventCharacterSwitch = false;

// pausing function prevents breaking html elements by keeping content untouched between certain strings
function setPause(charA, charB = false) {
  if (
     blockStart.indexOf(charA) > -1
  || blockEnd.indexOf(charA) > -1
  || pauseStrings.indexOf(charA) > -1
  || unpauseStrings.indexOf(charA) > -1

  || ( charB && (
       blockStart.indexOf(charB) > -1
    || blockEnd.indexOf(charB) > -1
    || pauseStrings.indexOf(charB) > -1
    || unpauseStrings.indexOf(charB) > -1)
     )
  ) preventCharacterSwitch = true;

  else preventCharacterSwitch = false;

  if (blockStart.indexOf(charA) > -1 || blockStart.indexOf(charB) > -1) blockPause = true;
  else if (blockEnd.indexOf(charA) > -1) blockPause = false;

  if (pauseStrings.indexOf(charA) > -1 || pauseStrings.indexOf(charB) > -1) pause = true;
  else if (unpauseStrings.indexOf(charA) > -1) pause = false;

//  return ((blockPause || pause || preventCharacterSwitch)?false:true);
}

let alphaSwaps = {
  // if using this mode, map characters to a random alternate
  "A" : "ɅÀÁÂÃÄÅĀĂĄǍǞǠǺȀȂȦȺΆΑΛΔАДӐӒԬᴀᴬḀẠẢẤẦẨẪẬẮẰẲẴẶἈἉἊἋἌἍἎἏᾈᾉᾊᾋᾌᾍᾎᾏᾸᾹᾺΆᾼⱯ",
  "a" : "@àáâãäāăąǎǻȁȃȧɐаӑӓᵃᵄḁẚạảấầẩẫậắằẳẵặἀἁἂἃἄἅἆἇὰάᾀᾁᾂᾃᾄᾅᾆᾇᾰᾱᾲᾳᾴᾶᾷₐꬰꭤ",
  "B" : "ßƁƂƄɃʙɮΒβϐБВвᴃᴮᴯᵦḂḄḆẞ₿",
  "b" : "ƀƃƅɓЪѢѣҌҍҔҕᵇᵬᶀḃḅḇ",
  "C" : "ĆĈĊČƇȻʗϽϿϾϹСҪ©",
  "c" : "¢ćĉçċčƈȼɔͻͼͽϲсҫᴄᴐᵓᶜḉ",
  "D" : "ÐĎĐƉƊᴅḊḌḎḐḒⱰᴰ",
  "d" : "ďƋƌđժᵈᵭᶁᶑḋḍḏḑḓ₫",
  "E" : "ÈÉÊËĒĔĖĘĚƎƐȄȆȨΈΕΞЀЁЕϵӖᴇᴱᴲḔḖḘḚḜẸẺẼẾỀỂỄỆἘἙἚἛἜἝ€ⱻ∑Ƹέεξ",
  "e" : "èéêëēĕėęěƏǝȅȇȩɇɘəɚѐёӗәӘӚӛᵉᵊḕḗḙḛḝẹẻẽếềểễệ℮ꬲꬳꬴҼҽҾ",
  "F" : "ƑҒբᵳḞ₣",
  "f" : "ƒɟʄғӻᵲᶠḟẜẝ",
  "G" : "ĜĞĠĢƓǤǦǴɢʛԌԍḠ₲",
  "g" : "ĝğġģǥǵǧɡɠᵍᵷᶃᶢḡ",
  "H" : "ĤĦȞʜҤԨԩḢḤḦḨḪἨἩἪἫἬἭἮἯᾘᾙᾚᾛᾜᾝᾞᾟῊΉῌⱧ",
  "h" : "ĥħȟɦɧҺһԦԧᶣᶙḣḥḧḩḫⱨ",
  "I" : "|¦ÌÍÎÏĨĪĬĮİȈȊΊΪІЇӏӀḬḮỈỊἸἹἺἻἼἽἾἿῘῙῚΊ",
  "i" : "¡ìíîïĩīĭįıǃǐȉȋɨɩɪΐίιϊіїᴉᵻᵼᶖᶤᶥḭḯỉịἰἲἳἴἵἶἷὶίῐῑῒΐῖῗꜟ",
  "J" : "ĴᴊᴶɈĵ",
  "j" : "ʝϳјᶨ",
  "K" : "ĶǨϏκΚҚҜҞҠᴋḰḲḴ₭Ⱪᴷ",
  "k" : "ķƙʞϗқҝҟҡԟᵏᶄḱḳḵⱪ",
  "L" : "ĹĻĽĿŁȽԼւᴌᴸᶫḸḺḼ∟£",
  "l" : "ĺļľŀłƚɭɬɫʅʆլᶅᶘᶪᶩḷḹḻḽⱡ",
  "M" : "ΜӍᴍᴹḾṀṂṄ₼Ɱ",
  "m" : "ɯɰɱʍϻмӎապᵐᶬᶆḿṁṃ₥",
  "N" : "ŃŅƝǸȠΝͶЍИЙийӢӣӤӥᴎṆṈṊ₦",
  "n" : "ńņňŉŋƞǹȵɲɳΠήПлпӆԓԥԯՈՌըղոռրᴖᴨᴫᵑᵰᶇᶮᶯṅṇṉṋἠἡἢἣἤἥἦἧὴήᾐᾑᾒᾓᾔᾕᾖᾗῂῃῄῆῇⁿ∩",
  "O" : "ÒÓÔÕÖØŌŎŐƟƠȌǑǪǬȎȪȬȮȰʘΌΘΟΦθϴОѺӦӨӪՕṌṎṐṒỌỎỐỒỔỖỘỚỜỞỠỢὈὉὊὋὌὍῸΌ",
  "o" : "ðòóôõöøōŏőơǒǫǭȍȏȫȭȯȱɵοσόϙоѳӧөӫօᴏᴑᴕᴼᵒᶱᶲᶿṍṏṑṓọỏốồổỗộớờởỡợὀὁὂὃὄὅὸόₒⱺ",
  "P" : "ƤРҎՔᴘᴩṔṖ₱₽Ᵽ",
  "p" : "ƥƿρҏԗթքᵖᶈṕṗ",
  "Q" : "ɊԚ",
  "q" : "ϤϥԛԳգզᶐ",
  "R" : "®ŔŖŘƦȐȒɌЯᴿṘṚṜṞ₹Ɽ",
  "r" : "ŕŗřȑȓɍɼɽɾʳгѓҐґӶӷԻՐᵣᶉṙṛṝṟ",
  "S" : "ŚŜŞŠƧȘϨЅՏՑֆṠṢṤṦṨ₷§$Ƽ",
  "s" : "śŝşšƨƽșȿʂϛѕᵴᶊᶳṡṣṥṧṩ",
  "T" : "ŢŤŦƬƮȚΤτТтҬᴛṪṬṮṰ₸₮",
  "t" : "ţťŧƫƭțʈʇϮϯҭԵԷեէᵵᶵṫṭṯṱẗ†",
  "U" : "ÙÚÛÜŨŪŬŮŰŲƯƱǓǕǗǙǛȔȖЏЦᵁṲṴṶṸṺỤỦỨỪỬỮỰ",
  "u" : "ùúûüũūŭůűųưǔǖǘǚǜȕȗʊϋύцҵնևսᴗᵕᶶᶷᶸṳṵṷṹṻὐὑὒὓὔὕὖὗụủứừửữựὺύῠῡῢΰῦῧ",
  "V" : "ѴѶᴠᶌṼ˅ͮѵѷ",
  "v" : "ᵥṽṿ√ⱱⱴ",
  "W" : "ŴϢШЩѠԜẀẂẄẆẈ₩Ⱳ",
  "w" : "ŵƜʷϣшщᴡẁẃẅẇẉὠὡὢὣὤὥὦὧὼώᾠᾡᾢᾣᾤᾥᾦᾧῲῳῴῶῷⱳ",
  "X" : "ΧЖҖҲӁӜӾẊẌ",
  "x" : "˟ˣжхӂӝӽӿᶍẋẍ",
  "Y" : "ŶŸƳƔȲɎΎΥΫϒϓϔЎУҮҰҶӮӰӲӴẎὙὛὝὟῨῩῪΎγ¥Ψ",
  "y" : "ýÿŷƴȳɏʎʏɤˠψЧучўүұҷҹӌӯӱӳӵẏỳỵỷỹỿ",
  "Z" : "ŹŻŽƵȤΖᴢẐẒẔⱫⱿ",
  "z" : "źżžƶʐʑᵶᶻᶼᶽẑẓẕⱬ"
}

// build the reverse object so we can run this multiple times
let alphaSwaps2 = {};

for (const x in alphaSwaps) {
  for (let c=0; c < alphaSwaps[x].length; c++) {
    alphaSwaps2[alphaSwaps[x].charAt(c)] = x;
  }
}

let charSwaps = {
// prevent breaking html entities
  "─":"&lt;",
  "│":"&gt;",
  "┌":"&reg;",
  "┐":"&copy;",
  "└":"&raquo;",
  "┘":"&laquo;",
  "├":"&amp;",
  "┤":"&nbsp;",
  "┬":"&mdash;",
  "┴":"&ndash;",
  "┼":"&quot;",
  "═":"&apos;",
  "║":"&trade;",
  "╒":"::before",
  "╓":"::after",

// block start
  "╔":"<noscript",
  "╕":"<script",
  "╖":"<!--",
  "╗":"<style>",

// block end
  "╘":"</noscript>",
  "╙":"</script>",
  "╚":"-->",
  "╛":"</style>"
};

function convertCopy(input, ransomNoteMode = false) {
  let wordphrase = input.innerHTML;
  let tempphrase = "";
  let outputphrase = "";

  Object.keys(charSwaps).forEach((key, index) => {
    wordphrase = wordphrase.replaceEach(charSwaps[key],key);
  });

  for (let i=0; i<wordphrase.length; i++) {
    let char = wordphrase.charAt(i);

    setPause(char);

    if (!blockPause && !pause) {
      // alphaSwap
      if (ransomNoteMode) {
        // allow us to rerun on already converted text
        if (alphaSwaps2[char] !== undefined) char = alphaSwaps2[char];
        if (alphaSwaps[char] !== undefined && getRnd(0,3) == 0) {
          let tempV = alphaSwaps[char];
          char = tempV.charAt(Math.floor(Math.random() * tempV.length))
        }
      }

      else char = (getRnd(0,1) == 0 ? char.toLowerCase() : char.toUpperCase());
    }


    tempphrase += char;
  }

  for (let t=0; t<tempphrase.length; t++) {
    let char1 = tempphrase.charAt(t);
    let char2 = tempphrase.charAt(t+1);
    let outChars = "";
    let sw = getRnd(0,10);
    //let sw = 1;

    setPause(char1, char2);

    if (sw == 0 && !(blockPause || pause || preventCharacterSwitch) && !ransomNoteMode && t+1 < tempphrase.length && !char1.match(/['"]/) && !char2.match(/['"]/)) {
      // swap this char and the next
      outChars = char2 + char1;
      t++;
    }

    else outChars = char1;

    outputphrase += outChars;
  }

  Object.keys(charSwaps).forEach((key, index) => {
    outputphrase = outputphrase.replaceEach(key,charSwaps[key]);
  });

  input.innerHTML = outputphrase;
}

function getRnd(min, max) {
  return Math.floor((Math.random() * (max - min + 1) ) + min);
}

// case-insensitive replace
String.prototype.replaceEach = function(strReplace, strWith) {
  let esc = strReplace.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
  let reg = new RegExp(esc, 'ig');
  return this.replace(reg, strWith);
};

// alt-click anywhere on a page to trigger
document.body.addEventListener('click', function(e) {
  if (e.altKey) {
    e.preventDefault();
    return false; }
  }, true);

document.body.addEventListener('mouseup', function(v) {
  if (v.altKey) {
    if (v.ctrlKey) convertCopy(v.target, true);
    else convertCopy(v.target);
  }
}, false);