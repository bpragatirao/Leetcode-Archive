# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        node1 = head
        node2 = head

        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next

            if node1 == node2:
                node1 = head
                while node1 != node2:
                    node1 = node1.next
                    node2 = node2.next
                return node1
        
        return None