/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    let left=0;
    let right=0;
    let vowels='aeiou';
    let maxVowels=0;
    let count=0;

    while(right<s.length) {
        if(vowels.includes(s[right])) count++;

        if(right-left+1<k) {
            right++;
        }
        else {
            maxVowels=Math.max(maxVowels,count);

            if(count==k) return k;
            
            if(vowels.includes(s[left])) count--;
            right++;
            left++;
        }
    }
    return maxVowels;
};