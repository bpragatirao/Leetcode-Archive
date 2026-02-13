# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        l = head
        def getMid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = getMid(head)
        r = mid.next
        mid.next = None

        l = self.sortList(l)
        r = self.sortList(r)

        def merge(l,r):
            node = ListNode(l)
            curr = node

            while l and r:
                if l.val < r.val:
                    curr.next = l
                    l = l.next
                else:
                    curr.next = r
                    r = r.next
                curr = curr.next

            curr.next = l or r
            return node.next

        return merge(l,r)


