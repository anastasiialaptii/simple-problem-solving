/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let left=0;
    let right=0;
    let maxAvg=-Infinity;
    let sum=0;

    while(right<nums.length){
        let windowSize=right-left+1;
      

        if (windowSize<k) {
              sum+=nums[right];
            right++;
        }
        else if(windowSize==k) {
            let avg=sum/k;
            maxAvg=Math.max(maxAvg, avg);

            sum-=nums[left];
            left++;
            right++;
        }
    }

    return maxAvg;
};

