class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1

        freq = list(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        
        arr=[]

        for value in freq:
            if k>0:
                arr.append(value[0])
                k-=1

        return arr

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        