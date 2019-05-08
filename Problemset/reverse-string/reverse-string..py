
# @Title: 反转字符串 (Reverse String)
# @Author: uraboer
# @Date: 2019-05-06 23:45:16
# @Runtime: 212 ms
# @Memory: 17.4 MB

#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 方法一：数组索引倒序，注意在原地修改s[:]
        s[:]=s[::-1]
        
        # 方法二：倒序函数，注意在原地修改s[:]
        # s[:]=reversed(s)

        # 方法三：以一半为界，前后交换
        # n=len(s)
        # for i in range(n//2):
        #     s[i],s[n-i-1]=s[n-i-1],s[i]



