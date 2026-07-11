# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        sorted_arr = []
        for i in range(len(lists)):
            current = lists[i]
            while current:
                sorted_arr.append(current.val)
                current = current.next
        
        sorted_arr = sorted(sorted_arr)
        new_list = ListNode()
        new_current = new_list

        for val in sorted_arr:
            new_current.next = ListNode(val)
            new_current = new_current.next
        
        return new_list.next