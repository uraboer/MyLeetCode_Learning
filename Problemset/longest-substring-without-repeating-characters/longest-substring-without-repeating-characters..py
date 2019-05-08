
# @Title: 无重复字符的最长子串 (Longest Substring Without Repeating Characters)
# @Author: uraboer
# @Date: 2018-07-06 17:34:10
# @Runtime: 120 ms
# @Memory: N/A

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        if s is None or len(s)==0:
            return res
        d={}
        start=0
        tmp=0
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=start:
                start=d[s[i]]+1
            tmp=i-start+1
            d[s[i]]=i
            res=max(res,tmp)
        return res
