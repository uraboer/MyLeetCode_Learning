
# @Title: 最长回文子串 (Longest Palindromic Substring)
# @Author: uraboer
# @Date: 2018-07-09 11:25:27
# @Runtime: 9412 ms
# @Memory: N/A

class Solution:
     def longestPalindrome(self, s):
        """
        :type s: str
        :type sr: str
        :rtype: str
        """
        sr = "".join(reversed(s))
        answerLen = 1
        try:
            answer = s[0]
        except:
            return None
        i = 0
        while i < len(s) - 1:
            plus = 2
            while sr.find(s[i:i+plus]) != -1 and plus <= len(s)-i:
                plus = plus + 1
            if plus-1 > answerLen:
                taskAnswer = s[i:i+plus-1]
                if taskAnswer == taskAnswer[::-1]:
                    answer = taskAnswer
                    answerLen = len(answer)
            i = i + 1
        return answer
        
