class Solution(object):
    def findMaxAverage(self, nums, k):
        max_avg=0.0
        avg=0
        for i in range(k):
            avg+=nums[i]
        max_avg=avg/float(k)
        for i in range(k,len(nums)):
            avg+=nums[i]
            avg-=nums[i-k]
            
            if max_avg<avg/float(k):
                max_avg=avg/float(k)
        return max_avg

