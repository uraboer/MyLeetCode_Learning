
# @Title: 计数二进制子串 (Count Binary Substrings)
# @Author: uraboer
# @Date: 2019-05-05 22:53:38
# @Runtime: 192 ms
# @Memory: 13.1 MB

#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 假设当前位置为1，前一个位置为0，初始子串个数为0
        count = 0
        pre = 0
        cur = 1
        # 遍历字符串
        for i in range(1, len(s)):
            # 如果当前位置字符和前一位置相等，则当前位置自增1
            if s[i] == s[i - 1]:
                cur += 1
            # 否则，把当前位置赋值为前一位置，当前位置重置为1 
            else:
                pre = cur
                cur = 1
            # 如果前面统计的个数大于等于后面的个数，则一定有符合的子串，加1
            if pre >= cur:
                count += 1
        return count


