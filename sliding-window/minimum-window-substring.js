/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let sLen=s.length;
    let tLen=t.length; // window

    if(sLen<tLen) return "";

    let right=0;
    let left=0;
    let set=new Set();
    let maxSubStr="";
    let subStr="";

    while(right<sLen) {
        if(t.includes(s[right])) {
            // subStr=subStr.concat(s[right]);
            // t.replace(s[right], '');
            left=right;
            break;
        }
        right++;
    }


    while(left<sLen) {
        subStr=subStr.concat(s[left]);

        if(t!=="" && t.includes(s[left])){
            t=t.replace(s[left], '');
        }

        if(t=="") {
            maxSubStr=subStr.length > maxSubStr.length ? subStr.length : maxSubStr.length;
            break;
        }

        right++;
    }

    subStr="";

    while(left<sLen) {
        subStr=subStr.concat(s[left]);

        if(t!=="" && t.includes(s[left])){
            t=t.replace(s[left], '');
        }

        if(t=="") {
            maxSubStr=subStr.length > maxSubStr.length ? subStr.length : maxSubStr.length;
        }
        if(right-left+1<maxSubStr.length) {
            while(right-left+1<maxSubStr.length) {
                left++;
            }
        }
        right++;
    }

    return maxSubStr;
};
minWindow("ADOBECODEBANC", "ABC");


///**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let sLen = s.length;
    let tLen = t.length;
    
    if (sLen < tLen) return ""; // If `s` is smaller than `t`, no such substring exists

    let left = 0, right = 0;
    let tCount = {};  // To store the frequency of characters in `t`
    let windowCount = {};  // To store the frequency of characters in the current window of `s`
    let minLength = Infinity;
    let minSubStr = "";

    // Build the frequency map for `t`
    for (let char of t) {
        tCount[char] = (tCount[char] || 0) + 1;
    }

    let required = Object.keys(tCount).length;  // Number of distinct characters in `t`
    let formed = 0;  // Number of characters fully matched

    // Start sliding the window
    while (right < sLen) {
        let rightChar = s[right];
        windowCount[rightChar] = (windowCount[rightChar] || 0) + 1;

        // If the current character matches the count in `t`, increment `formed`
        if (tCount[rightChar] && windowCount[rightChar] === tCount[rightChar]) {
            formed++;
        }

        // Try to shrink the window when we have a valid match
        while (left <= right && formed === required) {
            let leftChar = s[left];

            // If the current window is smaller, update `minSubStr`
            if (right - left + 1 < minLength) {
                minLength = right - left + 1;
                minSubStr = s.substring(left, right + 1);
            }

            // Now, shrink from the left
            windowCount[leftChar]--;
            if (tCount[leftChar] && windowCount[leftChar] < tCount[leftChar]) {
                formed--;  // We no longer have a valid match for this character
            }

            left++;  // Shrink the window from the left
        }

        right++;  // Expand the window by moving `right`
    }

    return minSubStr;
};
