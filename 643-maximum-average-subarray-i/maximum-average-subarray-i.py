class Solution(object):
    def findMaxAverage(self, nums, k):

        curr_sum=max_avg=sum(nums[:k])
        for i in range(k,len(nums)):
            curr_sum +=nums[i] - nums[i-k]
            max_avg=max(max_avg,curr_sum)
        return max_avg/float(k)

