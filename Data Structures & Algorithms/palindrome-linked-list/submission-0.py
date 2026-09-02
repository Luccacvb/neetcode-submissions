# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        new_list = []
        current = head

        while current:
            new_list.append(current.val)
            current = current.next

        return new_list == new_list[::-1]
