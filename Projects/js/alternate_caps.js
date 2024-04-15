const alternate_caps = (inputStr) => {
    let outputString = "";
    for (let i = 0; i < inputStr.length; i++) {
        outputString += (i % 2  == 0 ? inputStr[i].toUpperCase() : inputStr[i].toLowerCase());
    }
    return outputString;
};

console.log(alternate_caps("testing string :)"));
