
# @Title: Excel表列序号 (Excel Sheet Column Number)
# @Author: uraboer
# @Date: 2019-05-07 14:19:40
# @Runtime: 76 ms
# @Memory: 13.1 MB

#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#


class Solution:
    def titleToNumber(self, s: str) -> int:
        # 26的几次方 * 当前字母的值，再求和
        # (ord("Z")-ord("A")+1)=26
        return sum([(ord("Z")-ord("A")+1)**(len(s)-i-1)*(ord(x)-ord("A")+1) for i, x in enumerate(s)])

