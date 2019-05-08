
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: uraboer
# @Date: 2018-10-25 17:33:07
# @Runtime: 88 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=first=ListNode(0)
        
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
        if l1==None:
            head.next=l2
        if l2==None:
            head.next=l1
        
        return first.next

