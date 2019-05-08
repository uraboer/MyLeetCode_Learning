
# @Title: 存在重复元素 II (Contains Duplicate II)
# @Author: uraboer
# @Date: 2019-03-26 14:40:38
# @Runtime: 68 ms
# @Memory: 20.4 MB

#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (33.19%)
# Total Accepted:    10.6K
# Total Submissions: 31.3K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j
# 的差的绝对值最大为 k。
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#
# for i in range(len(nums)-k):
#     if nums[i]==nums[i+k]:
#         return True
#     else:
#         return False
#   × testcase: '[1,0,1,1]\n1'
#   × answer: false
#   × expected_answer: true
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for index,value in enumerate(nums):
            if value in d and index-d[value]<=k:
                return True
            d[value]=index
        return False




