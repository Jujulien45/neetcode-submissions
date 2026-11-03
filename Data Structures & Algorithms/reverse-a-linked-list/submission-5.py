# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        last_node = None
        current_head = head
        while current_head.next is not None:
            node = ListNode(current_head.val, last_node)
            current_head = current_head.next
            last_node = node

        node = ListNode(current_head.val, last_node)
        return node