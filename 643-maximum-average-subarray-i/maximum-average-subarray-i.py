class Solution(object):
    def findMaxAverage(self, nums, k):

        curr_sum=sum(nums[:k])
        max_avg=curr_sum/float(k)
        for i in range(k,len(nums)):
            curr_sum +=nums[i] - nums[i-k]
            max_avg=max(max_avg,curr_sum/float(k))
        return max_avg

