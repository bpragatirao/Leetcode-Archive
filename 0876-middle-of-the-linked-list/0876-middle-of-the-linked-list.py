# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        node = head
        new_node = head
        n,s = 0,0
        m = 0

        while node is not None:
            n+=1
            node = node.next

        if n%2==0:
            m = (n+1)//2
        else:
            m = n//2
        
        while new_node is not None:
            s += 1
            if s==m:
                return new_node.next
            new_node = new_node.next
