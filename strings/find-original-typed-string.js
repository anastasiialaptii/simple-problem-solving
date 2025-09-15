// 3330. Find the Original Typed String I

/**
 * @param {string} word
 * @return {number}
 */
var possibleStringCount = function(word) {
    let counter=1;

    for(let i=1; i<=word.length; i++) {
        if(word[i]==word[i-1]) {
            counter++;
        }
    }

    return counter;
};