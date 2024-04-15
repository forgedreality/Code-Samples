module.id = 'Logger';
console.log(__dirname);
console.log(__filename);

let url = 'http://mylogger.io/log'

const log = (message) => {
    // send http request
    console.log(message);
}

module.exports = log;