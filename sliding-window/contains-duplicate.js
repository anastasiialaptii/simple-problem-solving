var containsNearbyDuplicate = function(nums, k) {
    let numSet=new Set();

    for(let i=0; i<nums.length; i++){

        if(numSet.has(nums[i])) return true;
        
        numSet.add(nums[i]);

        if(i>=k){
            numSet.delete(nums[i-k]);
        }
    }

    return false;
};