# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head

        n = 1
        node = head
        while node.next:
            node = node.next
            n += 1

        node.next = head

        k = k % n
        steps = n - k
        
        new_node = head
        for i in range(steps - 1):
            new_node = new_node.next
            
        new_head = new_node.next
        new_node.next = None
        
        return new_head
