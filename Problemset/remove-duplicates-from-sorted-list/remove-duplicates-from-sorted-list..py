
# @Title: 删除排序链表中的重复元素 (Remove Duplicates from Sorted List)
# @Author: uraboer
# @Date: 2019-04-30 11:38:22
# @Runtime: 112 ms
# @Memory: 13 MB

#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (45.38%)
# Total Accepted:    25.3K
# Total Submissions: 55.7K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 链表为空
        if head is None:
            return head
        # 链表指向头部
        cur=head
        # 开始遍历链表
        while cur.next:
            # 如果当前值和下一位置值相等
            if cur.val==cur.next.val:
                # 把链表指向下下一位置（即删除）
                cur.next=cur.next.next
            else:
                # 否则，指向下一位置
                cur=cur.next
        # 返回链表
        return head



