// This is Comment

function concat(str1, str2) {
    return `${str1} - ${str2}`
}
concat = (str1, str2) => `${str1} - ${str2}`;

function checkLongStr(string) {
    if (string.length > 10) {
        return true
    }
    else {
        return false
    }
}
checkLongStr = string => {
    // if (string.length > 10) {
    //     return true
    // } else {
    //     return false
    // }
    return (string.length > 10) ? true : false
};

if (checkLongStr(concat('Happy', 'Hacking'))) {
    console.log('LONG STRING')
} else {
    console.log('SHORT STRING')
}
checkLongStr(concat('Happy', 'Hacking')) ? console.log('LONG STRING') : console.log('SHORT STRING');