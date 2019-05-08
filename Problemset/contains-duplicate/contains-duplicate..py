
# @Title: 存在重复元素 (Contains Duplicate)
# @Author: uraboer
# @Date: 2019-03-26 13:50:32
# @Runtime: 88 ms
# @Memory: 18.8 MB

#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (46.63%)
# Total Accepted:    47.7K
# Total Submissions: 100.4K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
# 
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: true
# 
# 示例 2:
# 
# 输入: [1,2,3,4]
# 输出: false
# 
# 示例 3:
# 
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
# 
#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums)==len(set(nums)) else True

# √ Accepted
#   √ 18/18 cases passed (68 ms)
#   √ Your runtime beats 30.71 % of python3 submissions
#   √ Your memory usage beats 0.84 % of python3 submissions (18.6 MB)


