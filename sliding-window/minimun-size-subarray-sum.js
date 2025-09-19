/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let subArrSum=0;
    let minSize=Infinity;
    let left=0;

    for(let right=0; right<nums.length; right++) {
        subArrSum+=nums[right];

        while(subArrSum>=target) {
            minSize=Math.min(minSize, right-left+1);
            subArrSum-=nums[left];
            left++;
        }
    }    

    return minSize === Infinity ? 0 : minSize;
};