
# @Title: 寻找两个有序数组的中位数 (Median of Two Sorted Arrays)
# @Author: uraboer
# @Date: 2018-07-07 22:57:59
# @Runtime: 132 ms
# @Memory: N/A

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=nums1+nums2
        res.sort()
        n=len(res)//2
        return res[n] if len(res)%2==1 else (res[n]+res[n-1])/2
