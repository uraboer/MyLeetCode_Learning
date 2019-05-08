
# @Title: 两数之和 (Two Sum)
# @Author: uraboer
# @Date: 2018-07-05 10:17:08
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            a=target-nums[i]
            if nums[i] in d:
                return d[nums[i]],i
            else:
                d[a]=i
