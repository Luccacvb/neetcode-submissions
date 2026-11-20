# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        new_list = []
        for node in lists:
            curr = node
            while curr:
                new_list.append(curr.val)
                curr = curr.next

        dummy = ListNode(0)
        new_linked = dummy
        for v in sorted(new_list):
            new_linked.next = ListNode(v)
            new_linked = new_linked.next

        return dummy.next
