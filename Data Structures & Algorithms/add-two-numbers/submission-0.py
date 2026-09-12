# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None

        cur1, cur2 = l1, l2
        dummy = ListNode()
        new_list = dummy
        carry = 0

        while cur1 and cur2:
            sum_nodes = cur1.val + cur2.val + carry
            carry = sum_nodes // 10
            sum_nodes = sum_nodes % 10

            new_list.next = ListNode(sum_nodes)
            cur1 = cur1.next
            cur2 = cur2.next
            new_list = new_list.next

        while cur1 or cur2:
            if cur1:
                sum_nodes = cur1.val + carry
                carry = sum_nodes // 10
                sum_nodes = sum_nodes % 10
                new_list.next = ListNode(sum_nodes)
                cur1 = cur1.next

            elif cur2:
                sum_nodes = cur2.val + carry
                carry = sum_nodes // 10
                sum_nodes = sum_nodes % 10
                new_list.next = ListNode(sum_nodes)
                cur2 = cur2.next

            new_list = new_list.next

        while carry > 0:
            sum_nodes = carry % 10
            carry = carry // 10
            new_list.next = ListNode(sum_nodes)
            new_list = new_list.next

        return dummy.next
