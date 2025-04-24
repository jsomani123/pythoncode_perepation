class Solution(object):
    def twoSum(self, nums, target):
        numToIndex={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in numToIndex:
                return numToIndex[compliment],i
            numToIndex[nums[i]]=i        