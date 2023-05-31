#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        while l1.next and l2.next:
            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10
            l1 = l1.next
            l2 = l2.next
        while l1.next:
            l1.val += carry
            carry = l1.val // 10
            l1.val %= 10
            l1 = l1.next
        while l2.next:
            l1.next = l2.next
            l1.val += carry
            carry = l1.val // 10
            l1.val %= 10
            l1 = l1.next
            l2 = l2.next
        l1.val += l2.val + carry
        carry = l1.val // 10
        l1.val %= 10
        if carry:
            l1.next = ListNode(carry)
        return l1


# @lc code=end
