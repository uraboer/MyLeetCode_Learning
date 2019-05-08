
# @Title: 组合总和 (Combination Sum)
# @Author: uraboer
# @Date: 2019-03-27 10:54:12
# @Runtime: 240 ms
# @Memory: 13.1 MB

#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (62.28%)
# Total Accepted:    13.7K
# Total Submissions: 21.6K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#


class Solution(object):
    def backtracking(self, candidates, target, start, val):
        if target == 0:
            Solution.re.append(val)
        else:
            for i in range(start,len(candidates)):
                if target < 0:
                    break
                self.backtracking(candidates,target-candidates[i],i,val+[candidates[i]])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.re = []
        self.backtracking(candidates,target,0,[])
        return Solution.re
# √ Accepted
#   √ 168/168 cases passed (220 ms)
#   √ Your runtime beats 21.1 % of python3 submissions
#   √ Your memory usage beats 0.88 % of python3 submissions (13.2 MB)
 

