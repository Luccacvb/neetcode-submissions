# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1 is None and list2 is None:
            return None

        cur1 = list1
        cur2 = list2
        new_list = ListNode(0)
        dummy = new_list

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                dummy.next = cur1
                cur1 = cur1.next
            else:
                dummy.next = cur2
                cur2 = cur2.next
            dummy = dummy.next

        if cur1 or cur2:
            dummy.next = cur1 or cur2

        return new_list.next
